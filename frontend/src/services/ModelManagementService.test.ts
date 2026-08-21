import { afterEach, describe, expect, it, vi } from "vitest";
import { AuthService } from "./AuthService";
import { ModelManagementService } from "./ModelManagementService";
import { ModelRecord } from "../types";

function authenticatedService(): { authService: AuthService; service: ModelManagementService } {
  const authService: AuthService = new AuthService("");
  authService.setApiKey("test-key");
  return {
    authService,
    service: new ModelManagementService(authService, ""),
  };
}

const modelRecord: ModelRecord = {
  id: 1,
  name: "qwen",
  path: "/models/qwen.gguf",
  repo: null,
  filename: null,
  size_bytes: 10,
  status: "ready",
  detail: "",
  created_at: "2026-08-21T00:00:00",
  exists: true,
  active: true,
};

describe("ModelManagementService", () => {
  afterEach(() => {
    vi.unstubAllGlobals();
  });

  it("lists models with provider health", async () => {
    const { service } = authenticatedService();
    const payload = {
      models: [modelRecord],
      providers: {
        active: { name: "local_llama_cpp", available: true },
        backup: null,
        consecutive_failures: 0,
      },
    };
    const fetchMock: ReturnType<typeof vi.fn> = vi
      .fn()
      .mockResolvedValue(new Response(JSON.stringify(payload), { status: 200 }));
    vi.stubGlobal("fetch", fetchMock);

    const result = await service.listModels();
    expect(result.models[0].name).toBe("qwen");
    expect(result.providers.active?.available).toBe(true);
    expect(fetchMock.mock.calls[0][0]).toBe("/admin/models");
  });

  it("registers a model from a server path", async () => {
    const { service } = authenticatedService();
    const fetchMock: ReturnType<typeof vi.fn> = vi
      .fn()
      .mockResolvedValue(new Response(JSON.stringify({ model: modelRecord }), { status: 201 }));
    vi.stubGlobal("fetch", fetchMock);

    const result = await service.registerModel("qwen", "/models/qwen.gguf");
    expect(result.model.id).toBe(1);
    const [url, init] = fetchMock.mock.calls[0] as [string, RequestInit];
    expect(url).toBe("/admin/models/register");
    expect(init.method).toBe("POST");
    expect(JSON.parse(String(init.body))).toEqual({ name: "qwen", path: "/models/qwen.gguf" });
  });

  it("queues a download", async () => {
    const { service } = authenticatedService();
    const fetchMock: ReturnType<typeof vi.fn> = vi.fn().mockResolvedValue(
      new Response(JSON.stringify({ status: "downloading", model: modelRecord }), {
        status: 202,
      }),
    );
    vi.stubGlobal("fetch", fetchMock);

    await service.downloadModel("n", "repo", "file.gguf");
    const [, init] = fetchMock.mock.calls[0] as [string, RequestInit];
    expect(JSON.parse(String(init.body))).toEqual({
      name: "n",
      repo: "repo",
      filename: "file.gguf",
    });
  });

  it("activates a model by id", async () => {
    const { service } = authenticatedService();
    const fetchMock: ReturnType<typeof vi.fn> = vi
      .fn()
      .mockResolvedValue(new Response(JSON.stringify({ model: modelRecord }), { status: 200 }));
    vi.stubGlobal("fetch", fetchMock);

    await service.activateModel(7);
    const [url] = fetchMock.mock.calls[0] as [string];
    expect(url).toBe("/admin/models/7/activate");
    expect((fetchMock.mock.calls[0] as [string, RequestInit])[1].method).toBe("POST");
  });

  it("deletes a registration", async () => {
    const { service } = authenticatedService();
    const fetchMock: ReturnType<typeof vi.fn> = vi
      .fn()
      .mockResolvedValue(new Response(JSON.stringify({ status: "ok" }), { status: 200 }));
    vi.stubGlobal("fetch", fetchMock);

    await service.deleteModel(3);
    expect(fetchMock.mock.calls[0][0]).toBe("/admin/models/3");
  });

  it("uploads a gguf file with its name in the query string", async () => {
    const { service } = authenticatedService();
    const fetchMock: ReturnType<typeof vi.fn> = vi
      .fn()
      .mockResolvedValue(new Response(JSON.stringify({ model: modelRecord }), { status: 201 }));
    vi.stubGlobal("fetch", fetchMock);

    const file: File = new File(["gguf"], "mymodel.gguf");
    await service.uploadModel("mymodel", file);
    const [url, init] = fetchMock.mock.calls[0] as [string, RequestInit];
    expect(url).toBe("/admin/models/upload?name=mymodel");
    expect(init.method).toBe("POST");
    expect(init.body).toBeInstanceOf(FormData);
  });

  it("reads, saves, and activates prompt versions", async () => {
    const { service } = authenticatedService();
    const fetchMock: ReturnType<typeof vi.fn> = vi.fn().mockImplementation(() =>
      Promise.resolve(
        new Response(JSON.stringify({ versions: [], template: "x", version_id: 5, status: "ok" }), {
          status: 200,
        }),
      ),
    );
    vi.stubGlobal("fetch", fetchMock);

    await service.updatePrompt("new rules");
    let [url, init] = fetchMock.mock.calls[0] as [string, RequestInit];
    expect(url).toBe("/admin/prompt");
    expect(init.method).toBe("PUT");

    await service.activatePromptVersion(9);
    [url] = fetchMock.mock.calls[1] as [string];
    expect(url).toBe("/admin/prompt/versions/9/activate");
  });

  it("throws ApiError with server detail on failure", async () => {
    const { service } = authenticatedService();
    const fetchMock: ReturnType<typeof vi.fn> = vi.fn().mockResolvedValue(
      new Response(JSON.stringify({ detail: "Only .gguf files can be uploaded" }), {
        status: 400,
      }),
    );
    vi.stubGlobal("fetch", fetchMock);

    await expect(service.registerModel("bad", "/nope")).rejects.toThrow(".gguf");
  });
});
