export type Verdict = "PASS" | "BLOCK" | "REVIEW";

export interface ModerationResponse {
    id?: string | null;
    verdict: Verdict;
    levelUsed: number;
    reasons: string[];
    matchedWords: string[];
    matchedLanguage?: string | null;
    confidenceScore?: number | null;
    latencyMs: number;
    detectorChain: string[];
}

export interface BatchModerationResponse {
    results: ModerationResponse[];
    totalLatencyMs: number;
}

export interface WordEntry {
    id: number;
    word: string;
    language: string;
    category: string;
    severity: number;
    createdAt: string;
}

export interface WordBankStats {
    totalWords: number;
    customWords: number;
    baseWords: number;
    languages: number;
    categories: number;
}

export interface DetectorStatus {
    name: string;
    available: boolean;
}

export interface HealthReport {
    status: string;
    uptimeSeconds: number;
    wordCount: WordBankStats;
    llamaAvailable: boolean;
    detectors: DetectorStatus[];
}

export type AuditEntry = Record<string, unknown>;

export interface LogFileInfo {
    name: string;
    size: number;
}

export interface LogContent {
    name: string;
    lines: number;
    tail: string[];
}

export interface WordPayload {
    word: string;
    language: string;
    category: string;
    severity: number;
}
