import { ApiError, AuthService } from "./AuthService";
import { AuditEntry, LogContent, LogFileInfo } from "../types";

export class AuditService {
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
            const detail: unknown =
                body !== null && typeof body === "object" && "detail" in body
                    ? (body as { detail: unknown }).detail
                    : "Request failed";
            throw new ApiError(response.status, String(detail));
        }
        return (await response.json()) as T;
    }

    public getAudit(): Promise<AuditEntry[]> {
        return this.request<AuditEntry[]>("/admin/wordbank/audit");
    }

    public listLogs(): Promise<LogFileInfo[]> {
        return this.request<LogFileInfo[]>("/admin/logs");
    }

    public getLog(filename: string): Promise<LogContent> {
        return this.request<LogContent>(`/admin/logs/${encodeURIComponent(filename)}`);
    }
}
