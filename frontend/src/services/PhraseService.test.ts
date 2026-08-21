import { afterEach, describe, expect, it, vi } from "vitest";
import { AuthService } from "./AuthService";
import { PhraseService } from "./PhraseService";
import { PhraseEntry, PhrasePayload } from "../types";

function authenticatedService(): { authService: AuthService; service: PhraseService } {
    const authService: AuthService = new AuthService("");
    authService.setApiKey("test-key");
    return { authService, service: new PhraseService(authService, "") };
}

const payload: PhrasePayload = {
    phrase: "bomb the building",
    language: "en",
    category: "violence",
    severity: 9,
};

describe("PhraseService", () => {
    afterEach(() => {
        vi.unstubAllGlobals();
    });

    it("adds a phrase and returns the typed entry", async () => {
        const { service } = authenticatedService();
        const created: PhraseEntry = {
            id: 1,
            phrase: "bomb the building",
            language: "en",
            category: "violence",
            severity: 9,
            created_at: "2026-08-13T10:00:00",
        };
        const fetchMock: ReturnType<typeof vi.fn> = vi
            .fn()
            .mockResolvedValue(new Response(JSON.stringify(created), { status: 201 }));
        vi.stubGlobal("fetch", fetchMock);

        const result: PhraseEntry = await service.add(payload);
        expect(result.id).toBe(1);
        expect(result.category).toBe("violence");

        const [url, init] = fetchMock.mock.calls[0] as [string, RequestInit];
        expect(url).toBe("/admin/phrases");
        expect(init.method).toBe("POST");
        expect(JSON.parse(String(init.body))).toEqual(payload);
    });

    it("lists phrases", async () => {
        const { service } = authenticatedService();
        const fetchMock: ReturnType<typeof vi.fn> = vi
            .fn()
            .mockResolvedValue(new Response(JSON.stringify([payload]), { status: 200 }));
        vi.stubGlobal("fetch", fetchMock);

        const result: PhraseEntry[] = await service.list();
        expect(result.length).toBe(1);
        expect(fetchMock.mock.calls[0][0]).toBe("/admin/phrases");
    });

    it("updates a phrase with a partial payload", async () => {
        const { service } = authenticatedService();
        const fetchMock: ReturnType<typeof vi.fn> = vi
            .fn()
            .mockResolvedValue(new Response(JSON.stringify(payload), { status: 200 }));
        vi.stubGlobal("fetch", fetchMock);

        await service.update(1, { severity: 10 });
        const [url, init] = fetchMock.mock.calls[0] as [string, RequestInit];
        expect(url).toBe("/admin/phrases/1");
        expect(init.method).toBe("PUT");
        expect(JSON.parse(String(init.body))).toEqual({ severity: 10 });
    });

    it("removes a phrase via query parameter", async () => {
        const { service } = authenticatedService();
        const fetchMock: ReturnType<typeof vi.fn> = vi
            .fn()
            .mockResolvedValue(new Response(JSON.stringify({ removed: true }), { status: 200 }));
        vi.stubGlobal("fetch", fetchMock);

        const result: { removed: boolean } = await service.remove(1);
        expect(result.removed).toBe(true);
        const [url, init] = fetchMock.mock.calls[0] as [string, RequestInit];
        expect(url).toBe("/admin/phrases?phrase_id=1");
        expect(init.method).toBe("DELETE");
    });

    it("rejects with the backend detail message", async () => {
        const { service } = authenticatedService();
        vi.stubGlobal(
            "fetch",
            vi.fn().mockResolvedValue(
                new Response(JSON.stringify({ detail: "phrase already exists" }), {
                    status: 409,
                }),
            ),
        );

        await expect(service.add(payload)).rejects.toThrow("phrase already exists");
    });
});
