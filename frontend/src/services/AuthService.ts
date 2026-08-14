export class ApiError extends Error {
    public readonly statusCode: number;

    public constructor(statusCode: number, message: string) {
        super(message);
        this.name = "ApiError";
        this.statusCode = statusCode;
    }
}

export function errorDetail(body: unknown, fallback: string): string {
    if (body !== null && typeof body === "object") {
        const record: Record<string, unknown> = body as Record<string, unknown>;
        if ("detail" in record) {
            return String(record.detail);
        }
        if ("error" in record) {
            return String(record.error);
        }
    }
    return fallback;
}

export class AuthService {
    private static readonly storageKey: string = "moderation_admin_api_key";

    private apiKey: string | null;

    private readonly unauthorizedHandlers: (() => void)[] = [];

    public constructor(private readonly baseUrl: string) {
        this.apiKey = localStorage.getItem(AuthService.storageKey);
    }

    public getApiKey(): string | null {
        return this.apiKey;
    }

    public setApiKey(key: string): void {
        this.apiKey = key;
        localStorage.setItem(AuthService.storageKey, key);
    }

    public clearApiKey(): void {
        this.apiKey = null;
        localStorage.removeItem(AuthService.storageKey);
    }

    public isAuthenticated(): boolean {
        return this.apiKey !== null && this.apiKey.length > 0;
    }

    public headers(): Record<string, string> {
        const base: Record<string, string> = { "Content-Type": "application/json" };
        if (this.apiKey !== null) {
            base["X-API-Key"] = this.apiKey;
        }
        return base;
    }

    public getBaseUrl(): string {
        return this.baseUrl;
    }

    public onUnauthorized(handler: () => void): () => void {
        this.unauthorizedHandlers.push(handler);
        return (): void => {
            const index: number = this.unauthorizedHandlers.indexOf(handler);
            if (index !== -1) {
                this.unauthorizedHandlers.splice(index, 1);
            }
        };
    }

    public handleUnauthorized(): void {
        if (this.apiKey === null) {
            return;
        }
        this.clearApiKey();
        for (const handler of this.unauthorizedHandlers) {
            handler();
        }
    }
}
