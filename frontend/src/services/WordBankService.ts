import { ApiError, AuthService } from "./AuthService";
import {
    WordBankStats,
    WordEntry,
    WordPayload,
} from "../types";

export class WordBankService {
    public constructor(
        private readonly authService: AuthService,
        private readonly apiBaseUrl: string,
    ) {}

    private async request<T>(path: string, init?: RequestInit): Promise<T> {
        const response: Response = await fetch(`${this.apiBaseUrl}${path}`, {
            ...init,
            headers: { ...this.authService.headers(), ...(init?.headers ?? {}) },
        });
        if (!response.ok) {
            const body: unknown = await response.json().catch(() => null);
            const detail: unknown =
                body !== null && typeof body === "object" && "detail" in body
                    ? (body as { detail: unknown }).detail
                    : "Request failed";
            throw new ApiError(response.status, String(detail));
        }
        if (response.status === 204) {
            return undefined as T;
        }
        return (await response.json()) as T;
    }

    public listWords(search?: string): Promise<WordEntry[]> {
        const query: string = search ? `?search=${encodeURIComponent(search)}` : "";
        return this.request<WordEntry[]>(`/admin/wordbank/words${query}`);
    }

    public addWord(payload: WordPayload): Promise<WordEntry> {
        return this.request<WordEntry>("/admin/wordbank/words", {
            method: "POST",
            body: JSON.stringify(payload),
        });
    }

    public removeWord(wordId: number): Promise<{ removed: boolean }> {
        return this.request<{ removed: boolean }>(
            `/admin/wordbank/words?word_id=${wordId}`,
            { method: "DELETE" },
        );
    }

    public updateWord(wordId: number, payload: Partial<WordPayload>): Promise<WordEntry> {
        return this.request<WordEntry>(`/admin/wordbank/words/${wordId}`, {
            method: "PUT",
            body: JSON.stringify(payload),
        });
    }

    public importWords(items: WordPayload[]): Promise<{ imported: number }> {
        return this.request<{ imported: number }>("/admin/wordbank/import", {
            method: "POST",
            body: JSON.stringify({ items }),
        });
    }

    public exportWords(): Promise<WordEntry[]> {
        return this.request<WordEntry[]>("/admin/wordbank/export");
    }

    public getStats(): Promise<WordBankStats> {
        return this.request<WordBankStats>("/admin/wordbank/stats");
    }

    public getLanguages(): Promise<string[]> {
        return this.request<string[]>("/admin/wordbank/languages");
    }

    public getCategories(): Promise<string[]> {
        return this.request<string[]>("/admin/wordbank/categories");
    }
}
