import { ApiError, AuthService, errorDetail } from "./AuthService";
import {
    DashboardReport,
    LoadTestConfig,
    LoadTestResult,
    ModerateDetailRequest,
    ModerateDetailResult,
    SettingRecord,
    StreamEvent,
    UserProfile,
} from "../types";

interface StreamOptions {
    method?: "GET" | "POST";
    body?: unknown;
    params?: Record<string, string>;
}

export class TestApiService {
    public constructor(
        private readonly authService: AuthService,
        private readonly apiBaseUrl: string,
    ) {}

    private async request<T>(path: string, init?: RequestInit): Promise<T> {
        const response: Response = await fetch(`${this.apiBaseUrl}${path}`, {
            ...init,
            headers: { ...this.authService.headers(), ...init?.headers },
        });
        if (!response.ok) {
            if (response.status === 401) {
                this.authService.handleUnauthorized();
            }
            const body: unknown = await response.json().catch(() => null);
            throw new ApiError(response.status, errorDetail(body, "Request failed"));
        }
        return (await response.json()) as T;
    }

    private async stream(
        path: string,
        options: StreamOptions,
        onEvent: (event: StreamEvent) => void,
    ): Promise<void> {
        const url: string =
            options.params !== undefined
                ? `${this.apiBaseUrl}${path}?${new URLSearchParams(options.params).toString()}`
                : `${this.apiBaseUrl}${path}`;
        const init: RequestInit = {
            method: options.method ?? "POST",
            headers: this.authService.headers(),
        };
        if (options.body !== undefined) {
            init.body = JSON.stringify(options.body);
        }
        const response: Response = await fetch(url, init);
        if (!response.ok) {
            if (response.status === 401) {
                this.authService.handleUnauthorized();
            }
            const raw: string = await response.text().catch(() => "");
            let detail: string = raw || "Request failed";
            try {
                detail = errorDetail(JSON.parse(raw), raw || "Request failed");
            } catch {
                // non-JSON body: surface the raw text as-is
            }
            throw new ApiError(response.status, detail);
        }
        if (response.body === null) {
            throw new ApiError(0, "Response has no body");
        }
        const reader: ReadableStreamDefaultReader<Uint8Array> = response.body.getReader();
        const decoder: TextDecoder = new TextDecoder();
        let buffer: string = "";
        let name: string | null = null;
        const dataLines: string[] = [];
        const dispatch = (): void => {
            if (name !== null) {
                onEvent({
                    name,
                    data: JSON.parse(dataLines.join("\n")) as Record<string, unknown>,
                });
            }
            name = null;
            dataLines.length = 0;
        };
        for (;;) {
            const { done, value } = await reader.read();
            if (done) {
                break;
            }
            buffer += decoder.decode(value, { stream: true });
            let newline: number;
            while ((newline = buffer.indexOf("\n")) !== -1) {
                const line: string = buffer.slice(0, newline).replace(/\r$/, "");
                buffer = buffer.slice(newline + 1);
                if (line.startsWith("event: ")) {
                    name = line.slice("event: ".length);
                } else if (line.startsWith("data: ")) {
                    dataLines.push(line.slice("data: ".length));
                } else if (line === "") {
                    dispatch();
                }
            }
        }
        if (name !== null) {
            dispatch();
        }
    }

    public async moderateDetail(
        payload: ModerateDetailRequest,
        onEvent: (event: StreamEvent) => void,
    ): Promise<ModerateDetailResult | null> {
        let result: ModerateDetailResult | null = null;
        await this.stream(
            "/test/moderate-detail?stream=true",
            { method: "POST", body: payload },
            (event) => {
                onEvent(event);
                if (event.name === "complete") {
                    result = event.data as unknown as ModerateDetailResult;
                }
            },
        );
        return result;
    }

    public async pipelineStatus(
        payload: ModerateDetailRequest,
        onEvent: (event: StreamEvent) => void,
    ): Promise<ModerateDetailResult | null> {
        let result: ModerateDetailResult | null = null;
        await this.stream(
            "/test/pipeline-status",
            {
                method: "GET",
                params: {
                    text: payload.text,
                    ...(payload.user_id !== undefined && payload.user_id !== null
                        ? { user_id: payload.user_id }
                        : {}),
                    ...(payload.app_name !== undefined && payload.app_name !== null
                        ? { app_name: payload.app_name }
                        : {}),
                },
            },
            (event) => {
                onEvent(event);
                if (event.name === "complete") {
                    result = event.data as unknown as ModerateDetailResult;
                }
            },
        );
        return result;
    }

    public async runLoadTest(
        config: LoadTestConfig,
        onEvent: (event: StreamEvent) => void,
    ): Promise<LoadTestResult | null> {
        let result: LoadTestResult | null = null;
        await this.stream("/test/load-test", { method: "POST", body: config }, (event) => {
            onEvent(event);
            if (event.name === "complete") {
                result = event.data as unknown as LoadTestResult;
            }
        });
        return result;
    }

    public getDashboard(): Promise<DashboardReport> {
        return this.request<DashboardReport>("/test/dashboard");
    }

    public getConfig(): Promise<{ settings: SettingRecord[] }> {
        return this.request<{ settings: SettingRecord[] }>("/test/config");
    }

    public updateConfig(settings: Record<string, string | number | boolean>): Promise<{
        status: string;
        updated: string[];
    }> {
        return this.request<{ status: string; updated: string[] }>("/test/config", {
            method: "POST",
            body: JSON.stringify({ settings }),
        });
    }

    public getUserProfile(appName: string, userId: string): Promise<UserProfile> {
        const params: URLSearchParams = new URLSearchParams({ app_name: appName, user_id: userId });
        return this.request<UserProfile>(`/test/user-profile?${params.toString()}`);
    }

    public seedUserProfile(
        appName: string,
        userId: string,
        totalMsgs: number,
        flaggedMsgs: number,
    ): Promise<{ status: string }> {
        return this.request<{ status: string }>("/test/user-profile/seed", {
            method: "POST",
            body: JSON.stringify({
                app_name: appName,
                user_id: userId,
                total_msgs: totalMsgs,
                flagged_msgs: flaggedMsgs,
            }),
        });
    }
}
