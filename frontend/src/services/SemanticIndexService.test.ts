import { afterEach, describe, expect, it, vi } from "vitest";
import { AuthService } from "./AuthService";
import { SemanticIndexService } from "./SemanticIndexService";
import { SemanticStatus } from "../types";

function authenticatedService(): {
    authService: AuthService;
    service: SemanticIndexService;
} {
    const authService: AuthService = new AuthService("");
    authService.setApiKey("test-key");
    return { authService, service: new SemanticIndexService(authService, "") };
}

const status: SemanticStatus = {
    available: true,
    ready: true,
    loading: false,
    model: "all-MiniLM-L6-v2",
    categories: { violence: 10, political: 10 },
};

describe("SemanticIndexService", () => {
    afterEach(() => {
        vi.unstubAllGlobals();
    });

    it("returns the semantic status", async () => {
        const { service } = authenticatedService();
        const fetchMock: ReturnType<typeof vi.fn> = vi
            .fn()
            .mockResolvedValue(new Response(JSON.stringify(status), { status: 200 }));
        vi.stubGlobal("fetch", fetchMock);

        const result: SemanticStatus = await service.getStatus();
        expect(result.available).toBe(true);
        expect(result.categories.violence).toBe(10);
        expect(fetchMock.mock.calls[0][0]).toBe("/admin/semantic");
    });

    it("lists supported categories", async () => {
        const { service } = authenticatedService();
        const fetchMock: ReturnType<typeof vi.fn> = vi.fn().mockResolvedValue(
            new Response(JSON.stringify({ categories: ["political", "violence"] }), {
                status: 200,
            }),
        );
        vi.stubGlobal("fetch", fetchMock);

        const result: string[] = await service.getCategories();
        expect(result).toEqual(["political", "violence"]);
        expect(fetchMock.mock.calls[0][0]).toBe("/admin/semantic/categories");
    });

    it("adds an example with an add action payload", async () => {
        const { service } = authenticatedService();
        const fetchMock: ReturnType<typeof vi.fn> = vi
            .fn()
            .mockResolvedValue(new Response(JSON.stringify({ status: "ok" }), { status: 200 }));
        vi.stubGlobal("fetch", fetchMock);

        await service.add("violence", "attack the school");
        const [url, init] = fetchMock.mock.calls[0] as [string, RequestInit];
        expect(url).toBe("/admin/semantic");
        expect(init.method).toBe("POST");
        expect(JSON.parse(String(init.body))).toEqual({
            action: "add",
            category: "violence",
            text: "attack the school",
        });
    });

    it("deletes an example with a delete action payload", async () => {
        const { service } = authenticatedService();
        const fetchMock: ReturnType<typeof vi.fn> = vi
            .fn()
            .mockResolvedValue(new Response(JSON.stringify({ status: "ok" }), { status: 200 }));
        vi.stubGlobal("fetch", fetchMock);

        await service.delete("political", "The government is corrupt");
        const [, init] = fetchMock.mock.calls[0] as [string, RequestInit];
        expect(JSON.parse(String(init.body))).toEqual({
            action: "delete",
            category: "political",
            text: "The government is corrupt",
        });
    });

    it("rejects with the backend detail message", async () => {
        const { service } = authenticatedService();
        vi.stubGlobal(
            "fetch",
            vi.fn().mockResolvedValue(
                new Response(
                    JSON.stringify({ detail: "Example not found in the category index" }),
                    {
                        status: 404,
                    },
                ),
            ),
        );

        await expect(service.delete("violence", "missing")).rejects.toThrow(
            "Example not found in the category index",
        );
    });
});
