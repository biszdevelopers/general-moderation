import { ApiError, AuthService, errorDetail } from "./AuthService";
import { PhraseEntry, PhrasePayload } from "../types";

export class PhraseService {
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

    public list(): Promise<PhraseEntry[]> {
        return this.request<PhraseEntry[]>("/admin/phrases");
    }

    public add(payload: PhrasePayload): Promise<PhraseEntry> {
        return this.request<PhraseEntry>("/admin/phrases", {
            method: "POST",
            body: JSON.stringify(payload),
        });
    }

    public update(phraseId: number, payload: Partial<PhrasePayload>): Promise<PhraseEntry> {
        return this.request<PhraseEntry>(`/admin/phrases/${phraseId}`, {
            method: "PUT",
            body: JSON.stringify(payload),
        });
    }

    public remove(phraseId: number): Promise<{ removed: boolean }> {
        return this.request<{ removed: boolean }>(`/admin/phrases?phrase_id=${phraseId}`, {
            method: "DELETE",
        });
    }
}
