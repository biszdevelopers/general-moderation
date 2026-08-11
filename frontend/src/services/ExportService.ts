import { ApiError, AuthService } from "./AuthService";

export class ExportService {
    public constructor(
        private readonly authService: AuthService,
        private readonly apiBaseUrl: string,
    ) {}

    public downloadExport(): Promise<Blob> {
        return fetch(`${this.apiBaseUrl}/admin/export`, {
            method: "GET",
            headers: { ...this.authService.headers() },
        }).then((response: Response): Promise<Blob> => {
            if (!response.ok) {
                return response
                    .json()
                    .catch(() => null)
                    .then((body: unknown): Promise<Blob> => {
                        const detail: unknown =
                            body !== null && typeof body === "object" && "detail" in body
                                ? (body as { detail: unknown }).detail
                                : "Export failed";
                        throw new ApiError(response.status, String(detail));
                    });
            }
            return response.blob();
        });
    }
}
