import { ApiError, AuthService, errorDetail } from "./AuthService";

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
                if (response.status === 401) {
                    this.authService.handleUnauthorized();
                }
                return response
                    .json()
                    .catch(() => null)
                    .then((body: unknown): Promise<Blob> => {
                        throw new ApiError(response.status, errorDetail(body, "Export failed"));
                    });
            }
            return response.blob();
        });
    }
}
