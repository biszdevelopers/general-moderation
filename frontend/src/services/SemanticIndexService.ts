import { ApiError, AuthService, errorDetail } from "./AuthService";
import { SemanticStatus } from "../types";

export class SemanticIndexService {
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

    public getStatus(): Promise<SemanticStatus> {
        return this.request<SemanticStatus>("/admin/semantic");
    }

    public async getCategories(): Promise<string[]> {
        const result: { categories: string[] } = await this.request<{ categories: string[] }>(
            "/admin/semantic/categories",
        );
        return result.categories;
    }

    public add(category: string, text: string): Promise<{ status: string }> {
        return this.request<{ status: string }>("/admin/semantic", {
            method: "POST",
            body: JSON.stringify({ action: "add", category, text }),
        });
    }

    public delete(category: string, text: string): Promise<{ status: string }> {
        return this.request<{ status: string }>("/admin/semantic", {
            method: "POST",
            body: JSON.stringify({ action: "delete", category, text }),
        });
    }
}
