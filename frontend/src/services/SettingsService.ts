import { ApiError, AuthService } from "./AuthService";
import { HealthReport } from "../types";

export class SettingsService {
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

    public getHealth(): Promise<HealthReport> {
        return this.request<HealthReport>("/admin/health");
    }

    public getMetrics(): Promise<string> {
        return this.request<string>("/admin/metrics");
    }

    public reload(): Promise<{ status: string }> {
        return this.request<{ status: string }>("/admin/reload", { method: "POST" });
    }

    public shutdown(): Promise<{ status: string }> {
        return this.request<{ status: string }>("/admin/shutdown", { method: "POST" });
    }
}
