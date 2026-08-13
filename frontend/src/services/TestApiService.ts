import { ApiError, AuthService } from "./AuthService";
import {
    DashboardReport,
    LoadTestConfig,
    LoadTestResult,
    ModerateDetailResult,
    SettingRecord,
    StreamEvent,
    UserProfile,
} from "../types";

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
            const body: unknown = await response.json().catch(() => null);
            const detail: unknown =
                body !== null && typeof body === "object" && "detail" in body
                    ? (body as { detail: unknown }).detail
                    : "Request failed";
            throw new ApiError(response.status, String(detail));
        }
        return (await response.json()) as T;
    }

    private async stream(
        path: string,
        body: unknown,
        onEvent: (event: StreamEvent) => void,
    ): Promise<void> {
        const response: Response = await fetch(`${this.apiBaseUrl}${path}`, {
            method: "POST",
            headers: this.authService.headers(),
            body: JSON.stringify(body),
        });
        if (!response.ok) {
            const detail: unknown = await response.text().catch(() => "");
            throw new ApiError(response.status, String(detail || "Request failed"));
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
        payload: { text: string; userId?: string; appName?: string },
        onEvent: (event: StreamEvent) => void,
    ): Promise<ModerateDetailResult | null> {
        let result: ModerateDetailResult | null = null;
        await this.stream("/test/moderate-detail?stream=true", payload, (event) => {
            onEvent(event);
            if (event.name === "complete") {
                result = event.data as unknown as ModerateDetailResult;
            }
        });
        return result;
    }

    public async runLoadTest(
        config: LoadTestConfig,
        onEvent: (event: StreamEvent) => void,
    ): Promise<LoadTestResult | null> {
        let result: LoadTestResult | null = null;
        await this.stream("/test/load-test", config, (event) => {
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
