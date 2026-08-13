import { ApiError, AuthService, errorDetail } from "./AuthService";
import { HealthReport, SettingRecord, TuneReport } from "../types";

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
            if (response.status === 401) {
                this.authService.handleUnauthorized();
            }
            const body: unknown = await response.json().catch(() => null);
            throw new ApiError(response.status, errorDetail(body, "Request failed"));
        }
        return (await response.json()) as T;
    }

    public getHealth(): Promise<HealthReport> {
        return this.request<HealthReport>("/admin/health");
    }

    public async getMetrics(): Promise<string> {
        const response: Response = await fetch(`${this.apiBaseUrl}/admin/metrics`, {
            headers: this.authService.headers(),
        });
        if (!response.ok) {
            if (response.status === 401) {
                this.authService.handleUnauthorized();
            }
            const body: unknown = await response.json().catch(() => null);
            throw new ApiError(response.status, errorDetail(body, "Request failed"));
        }
        return response.text();
    }

    public reload(): Promise<{ status: string }> {
        return this.request<{ status: string }>("/admin/reload", { method: "POST" });
    }

    public shutdown(): Promise<{ status: string }> {
        return this.request<{ status: string }>("/admin/shutdown", { method: "POST" });
    }

    public getSettings(): Promise<{ settings: SettingRecord[] }> {
        return this.request<{ settings: SettingRecord[] }>("/admin/settings");
    }

    public updateSettings(settings: Record<string, string | number | boolean>): Promise<{
        status: string;
        updated: string[];
    }> {
        return this.request<{ status: string; updated: string[] }>("/admin/settings", {
            method: "POST",
            body: JSON.stringify({ settings }),
        });
    }

    public runTuning(): Promise<TuneReport> {
        return this.request<TuneReport>("/admin/tune", { method: "POST" });
    }
}
