import { afterEach, describe, expect, it, vi } from "vitest";
import { AuthService } from "./AuthService";
import { SettingsService } from "./SettingsService";
import { ConfigPreset, SettingRecord } from "../types";

function authenticatedService(): { authService: AuthService; service: SettingsService } {
  const authService: AuthService = new AuthService("");
  authService.setApiKey("test-key");
  return { authService, service: new SettingsService(authService, "") };
}

describe("SettingsService configuration extensions", () => {
  afterEach(() => {
    vi.unstubAllGlobals();
  });

  it("queries history with key filter and limit", async () => {
    const { service } = authenticatedService();
    const fetchMock: ReturnType<typeof vi.fn> = vi
      .fn()
      .mockResolvedValue(new Response(JSON.stringify({ history: [] }), { status: 200 }));
    vi.stubGlobal("fetch", fetchMock);

    await service.getHistory("AI_TARGET_PERCENTAGE", 25);
    expect(fetchMock.mock.calls[0][0]).toBe(
      "/admin/settings/history?limit=25&key=AI_TARGET_PERCENTAGE",
    );
  });

  it("omits the key parameter when unset", async () => {
    const { service } = authenticatedService();
    const fetchMock: ReturnType<typeof vi.fn> = vi
      .fn()
      .mockResolvedValue(new Response(JSON.stringify({ history: [] }), { status: 200 }));
    vi.stubGlobal("fetch", fetchMock);

    await service.getHistory();
    expect(fetchMock.mock.calls[0][0]).toBe("/admin/settings/history?limit=100");
  });

  it("lists presets", async () => {
    const { service } = authenticatedService();
    const preset: ConfigPreset = {
      name: "Strict",
      description: "d",
      payload: { AI_TARGET_PERCENTAGE: 15 },
    };
    const fetchMock: ReturnType<typeof vi.fn> = vi
      .fn()
      .mockResolvedValue(new Response(JSON.stringify({ presets: [preset] }), { status: 200 }));
    vi.stubGlobal("fetch", fetchMock);

    const result = await service.getPresets();
    expect(result.presets[0].name).toBe("Strict");
  });

  it("creates a preset with a JSON body", async () => {
    const { service } = authenticatedService();
    const fetchMock: ReturnType<typeof vi.fn> = vi
      .fn()
      .mockResolvedValue(new Response(JSON.stringify({ status: "ok" }), { status: 201 }));
    vi.stubGlobal("fetch", fetchMock);

    await service.createPreset("Mine", "desc", { AI_TARGET_PERCENTAGE: 5 });
    const [, init] = fetchMock.mock.calls[0] as [string, RequestInit];
    expect(init.method).toBe("POST");
    expect(JSON.parse(String(init.body))).toEqual({
      name: "Mine",
      description: "desc",
      payload: { AI_TARGET_PERCENTAGE: 5 },
    });
  });

  it("applies and deletes presets by encoded name", async () => {
    const { service } = authenticatedService();
    const fetchMock: ReturnType<typeof vi.fn> = vi
      .fn()
      .mockImplementation(() =>
        Promise.resolve(
          new Response(JSON.stringify({ status: "ok", updated: [] }), { status: 200 }),
        ),
      );
    vi.stubGlobal("fetch", fetchMock);

    await service.applyPreset("High Accuracy");
    expect(fetchMock.mock.calls[0][0]).toBe("/admin/presets/High%20Accuracy/apply");
    await service.deletePreset("High Accuracy");
    expect(fetchMock.mock.calls[1][0]).toBe("/admin/presets/High%20Accuracy");
  });

  it("carries validation metadata on settings records", async () => {
    const { service } = authenticatedService();
    const record: SettingRecord = {
      key: "LLM_PROVIDER",
      value: "local_llama_cpp",
      type: "string",
      description: "Active provider",
      editable: true,
      category: "Models & Providers",
      restart_required: false,
      secret: false,
      choices: ["local_llama_cpp", "ollama"],
    };
    const fetchMock: ReturnType<typeof vi.fn> = vi
      .fn()
      .mockResolvedValue(new Response(JSON.stringify({ settings: [record] }), { status: 200 }));
    vi.stubGlobal("fetch", fetchMock);

    const result: { settings: SettingRecord[] } = await service.getSettings();
    expect(result.settings.length).toBe(1);
    expect(result.settings[0].category).toBe("Models & Providers");
    expect(result.settings[0].choices?.length).toBe(2);
  });
});
