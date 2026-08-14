import { afterEach, describe, expect, it, vi } from "vitest";
import { AuthService } from "./AuthService";
import { WordBankService } from "./WordBankService";
import { WordEntry, WordPayload } from "../types";

function authenticatedService(): { authService: AuthService; service: WordBankService } {
    const authService: AuthService = new AuthService("");
    authService.setApiKey("test-key");
    return { authService, service: new WordBankService(authService, "") };
}

const payload: WordPayload = {
    word: "badword",
    language: "en",
    category: "profanity",
    severity: 5,
};

describe("WordBankService", () => {
    afterEach(() => {
        vi.unstubAllGlobals();
    });

    it("adds a word and returns the typed entry", async () => {
        const { service } = authenticatedService();
        const created: WordEntry = {
            id: 1,
            word: "badword",
            language: "en",
            category: "profanity",
            severity: 5,
            createdAt: "2026-08-13T10:00:00",
        };
        const fetchMock: ReturnType<typeof vi.fn> = vi
            .fn()
            .mockResolvedValue(new Response(JSON.stringify(created), { status: 200 }));
        vi.stubGlobal("fetch", fetchMock);

        const result: WordEntry = await service.addWord(payload);
        expect(result.id).toBe(1);
        expect(result.category).toBe("profanity");

        const [url, init] = fetchMock.mock.calls[0] as [string, RequestInit];
        expect(url).toBe("/admin/wordbank/words");
        expect(init.method).toBe("POST");
        expect(JSON.parse(String(init.body))).toEqual(payload);
    });

    it("lists words with a search term", async () => {
        const { service } = authenticatedService();
        const fetchMock: ReturnType<typeof vi.fn> = vi
            .fn()
            .mockResolvedValue(new Response(JSON.stringify([payload]), { status: 200 }));
        vi.stubGlobal("fetch", fetchMock);

        const result: WordEntry[] = await service.listWords("bad");
        expect(result.length).toBe(1);
        expect(fetchMock.mock.calls[0][0]).toBe("/admin/wordbank/words?search=bad");
    });

    it("rejects with the backend detail message", async () => {
        const { service } = authenticatedService();
        vi.stubGlobal(
            "fetch",
            vi.fn().mockResolvedValue(
                new Response(JSON.stringify({ detail: "word already exists" }), {
                    status: 409,
                }),
            ),
        );

        await expect(service.addWord(payload)).rejects.toThrow("word already exists");
    });
});
