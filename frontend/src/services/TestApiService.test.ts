import { afterEach, describe, expect, it, vi } from "vitest";
import { AuthService } from "./AuthService";
import { TestApiService } from "./TestApiService";
import { ModerateDetailResult, SettingRecord, StreamEvent } from "../types";

function sseResponse(frames: [string, unknown][]): Response {
    const body: string = frames
        .map(([name, data]) => `event: ${name}\ndata: ${JSON.stringify(data)}\n\n`)
        .join("");
    return new Response(body, {
        status: 200,
        headers: { "Content-Type": "text/event-stream" },
    });
}

const completePayload: unknown = {
    response: {
        id: null,
        verdict: "BLOCK",
        allowed: false,
        levelUsed: 1,
        aiTriggered: false,
        suspicionScore: 30,
        reasons: ["Exact sensitive word matched in Aho-Corasick automaton"],
        reason: "Exact sensitive word matched in Aho-Corasick automaton",
        matchedWords: ["badword"],
        matchedWord: "badword",
        matchedLanguage: null,
        confidenceScore: 1,
        latencyMs: 3.2,
        detectorChain: ["bloom_filter", "rolling_hash", "aho_corasick"],
    },
    trace: {
        request_id: null,
        app_name: "default",
        user_id: "u1",
        text: "badword",
        verdict: "BLOCK",
        suspicion_score: 30,
        level_used: 1,
        ai_triggered: false,
        reasons: ["Exact sensitive word matched in Aho-Corasick automaton"],
        matched_words: ["badword"],
        matched_language: null,
        confidence_score: 1,
        stage_1: { fast_path: false, verdict: "BLOCK", latency_ms: 0.11 },
        stage_2: {
            detector_results: [
                {
                    name: "aho_corasick",
                    enabled: true,
                    available: true,
                    matched: true,
                    blocking: true,
                    confidence: 1,
                    matched_words: ["badword"],
                    matched_language: null,
                    reason: "Exact sensitive word matched in Aho-Corasick automaton",
                    latency_ms: 0.02,
                    weight: 30,
                },
            ],
            semantic_similarities: {},
            semantic_enabled: false,
            user_profile: null,
            suspicion_score: 30,
            weight_contributions: [],
            latency_ms: 1.2,
        },
        stage_3: null,
        total_latency_ms: 3.2,
    },
};

function authenticatedService(): { authService: AuthService; service: TestApiService } {
    const authService: AuthService = new AuthService("");
    authService.setApiKey("test-key");
    return { authService, service: new TestApiService(authService, "") };
}

describe("TestApiService", () => {
    afterEach(() => {
        vi.unstubAllGlobals();
    });

    it("parses SSE frames in order and returns the complete typed result", async () => {
        const { service } = authenticatedService();
        const fetchMock: ReturnType<typeof vi.fn> = vi.fn().mockResolvedValue(
            sseResponse([
                [
                    "stage1_complete",
                    { stage: 1, fast_path: false, verdict: "REVIEW", latency_ms: 0.11 },
                ],
                [
                    "detector_result",
                    {
                        name: "aho_corasick",
                        matched: true,
                        blocking: true,
                        confidence: 1,
                        matched_words: ["badword"],
                        reason: "Exact sensitive word matched in Aho-Corasick automaton",
                        latency_ms: 0.02,
                    },
                ],
                ["stage2_complete", { stage: 2, suspicion_score: 30, latency_ms: 1.2 }],
                ["stage3_complete", { stage: 3, invoked: false }],
                ["complete", completePayload],
            ]),
        );
        vi.stubGlobal("fetch", fetchMock);

        const names: string[] = [];
        const result: ModerateDetailResult | null = await service.moderateDetail(
            { text: "badword", user_id: "u1" },
            (event: StreamEvent) => names.push(event.name),
        );

        expect(names).toEqual([
            "stage1_complete",
            "detector_result",
            "stage2_complete",
            "stage3_complete",
            "complete",
        ]);
        expect(result?.response.verdict).toBe("BLOCK");
        expect(result?.trace.verdict).toBe("BLOCK");
        expect(result?.trace.stage_2.detector_results[0].weight).toBe(30);

        const [url, init] = fetchMock.mock.calls[0] as [string, RequestInit];
        expect(url).toBe("/test/moderate-detail?stream=true");
        expect(init.method).toBe("POST");
        expect(JSON.parse(String(init.body))).toEqual({ text: "badword", user_id: "u1" });
        expect((init.headers as Record<string, string> | undefined)?.["X-API-Key"]).toBe(
            "test-key",
        );
    });

    it("streams pipeline-status as a GET with query parameters", async () => {
        const { service } = authenticatedService();
        const fetchMock: ReturnType<typeof vi.fn> = vi
            .fn()
            .mockResolvedValue(sseResponse([["complete", completePayload]]));
        vi.stubGlobal("fetch", fetchMock);

        await service.pipelineStatus(
            { text: "hello", user_id: "u1", app_name: "web" },
            () => undefined,
        );

        const [url, init] = fetchMock.mock.calls[0] as [string, RequestInit];
        expect(url).toBe("/test/pipeline-status?text=hello&user_id=u1&app_name=web");
        expect(init.method).toBe("GET");
    });

    it("returns a typed settings catalog from GET /test/config", async () => {
        const { service } = authenticatedService();
        const settings: SettingRecord[] = [
            {
                key: "WEIGHT_DETECTOR_AHO",
                value: 30,
                type: "integer",
                description: "Suspicion weight",
                editable: true,
            },
        ];
        vi.stubGlobal(
            "fetch",
            vi.fn().mockResolvedValue(new Response(JSON.stringify({ settings }), { status: 200 })),
        );

        const result: { settings: SettingRecord[] } = await service.getConfig();
        expect(result.settings[0].key).toBe("WEIGHT_DETECTOR_AHO");
        expect(result.settings[0].value).toBe(30);
    });

    it("sends a settings batch to POST /test/config", async () => {
        const { service } = authenticatedService();
        const fetchMock: ReturnType<typeof vi.fn> = vi.fn().mockResolvedValue(
            new Response(JSON.stringify({ status: "ok", updated: ["WEIGHT_DETECTOR_AHO"] }), {
                status: 200,
            }),
        );
        vi.stubGlobal("fetch", fetchMock);

        const result: { status: string; updated: string[] } = await service.updateConfig({
            WEIGHT_DETECTOR_AHO: 35,
        });
        expect(result.updated).toEqual(["WEIGHT_DETECTOR_AHO"]);

        const [url, init] = fetchMock.mock.calls[0] as [string, RequestInit];
        expect(url).toBe("/test/config");
        expect(init.method).toBe("POST");
        expect(JSON.parse(String(init.body))).toEqual({ settings: { WEIGHT_DETECTOR_AHO: 35 } });
    });

    it("clears authentication when the backend returns 401", async () => {
        const { authService, service } = authenticatedService();
        let notified: boolean = false;
        authService.onUnauthorized(() => {
            notified = true;
        });
        vi.stubGlobal(
            "fetch",
            vi.fn().mockResolvedValue(
                new Response(JSON.stringify({ detail: "Invalid or missing API key" }), {
                    status: 401,
                }),
            ),
        );

        await expect(service.getDashboard()).rejects.toThrow("Invalid or missing API key");
        expect(notified).toBe(true);
        expect(authService.isAuthenticated()).toBe(false);
    });

    it("surfaces backend errors for streamed requests", async () => {
        const { service } = authenticatedService();
        vi.stubGlobal(
            "fetch",
            vi.fn().mockResolvedValue(
                new Response(JSON.stringify({ detail: "Rate limit exceeded" }), {
                    status: 429,
                }),
            ),
        );

        await expect(service.moderateDetail({ text: "hi" }, () => undefined)).rejects.toThrow(
            "Rate limit exceeded",
        );
    });

    it("parses the slowapi error key as the failure detail", async () => {
        const { service } = authenticatedService();
        vi.stubGlobal(
            "fetch",
            vi.fn().mockResolvedValue(
                new Response(JSON.stringify({ error: "Rate limit exceeded: 100 per 60 second" }), {
                    status: 429,
                }),
            ),
        );

        await expect(service.getDashboard()).rejects.toThrow(
            "Rate limit exceeded: 100 per 60 second",
        );
    });
});
