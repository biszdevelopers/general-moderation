import { ApiError, AuthService, errorDetail } from "./AuthService";
import { ModelRecord, PromptVersionRecord, ProviderHealthReport, SettingRecord } from "../types";

export class ModelManagementService {
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

  public listModels(): Promise<{ models: ModelRecord[]; providers: ProviderHealthReport }> {
    return this.request<{ models: ModelRecord[]; providers: ProviderHealthReport }>(
      "/admin/models",
    );
  }

  public getProviderHealth(): Promise<ProviderHealthReport> {
    return this.request<ProviderHealthReport>("/admin/models/health");
  }

  public registerModel(name: string, path: string): Promise<{ model: ModelRecord }> {
    return this.request<{ model: ModelRecord }>("/admin/models/register", {
      method: "POST",
      body: JSON.stringify({ name, path }),
    });
  }

  public downloadModel(
    name: string,
    repo: string,
    filename: string,
  ): Promise<{ status: string; model: ModelRecord }> {
    return this.request<{ status: string; model: ModelRecord }>("/admin/models/download", {
      method: "POST",
      body: JSON.stringify({ name, repo, filename }),
    });
  }

  public async uploadModel(name: string, file: File): Promise<{ model: ModelRecord }> {
    const body: FormData = new FormData();
    body.append("file", file);
    return this.request<{ model: ModelRecord }>(
      `/admin/models/upload?name=${encodeURIComponent(name)}`,
      { method: "POST", body },
    );
  }

  public activateModel(modelId: number): Promise<{ model: ModelRecord }> {
    return this.request<{ model: ModelRecord }>(`/admin/models/${modelId}/activate`, {
      method: "POST",
    });
  }

  public deleteModel(modelId: number): Promise<{ status: string }> {
    return this.request<{ status: string }>(`/admin/models/${modelId}`, { method: "DELETE" });
  }

  public getPrompt(): Promise<{ template: string }> {
    return this.request<{ template: string }>("/admin/prompt");
  }

  public updatePrompt(template: string): Promise<{ status: string; version_id: number }> {
    return this.request<{ status: string; version_id: number }>("/admin/prompt", {
      method: "PUT",
      body: JSON.stringify({ template }),
    });
  }

  public listPromptVersions(): Promise<{ versions: PromptVersionRecord[] }> {
    return this.request<{ versions: PromptVersionRecord[] }>("/admin/prompt/versions");
  }

  public activatePromptVersion(versionId: number): Promise<{ status: string }> {
    return this.request<{ status: string }>(`/admin/prompt/versions/${versionId}/activate`, {
      method: "POST",
    });
  }

  public async getSettings(): Promise<SettingRecord[]> {
    const result: { settings: SettingRecord[] } = await this.request<{
      settings: SettingRecord[];
    }>("/admin/settings");
    return result.settings;
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
}
