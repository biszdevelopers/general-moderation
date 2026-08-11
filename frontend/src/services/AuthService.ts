export class ApiError extends Error {
    public readonly statusCode: number;

    public constructor(statusCode: number, message: string) {
        super(message);
        this.name = "ApiError";
        this.statusCode = statusCode;
    }
}

export class AuthService {
    private static readonly storageKey: string = "moderation_admin_api_key";

    private apiKey: string | null;

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
}
