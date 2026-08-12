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

export interface SettingRecord {
    key: string;
    value: string | number | boolean;
    type: string;
    description: string;
    editable: boolean;
}

export interface AppConfigRecord {
    app_name: string;
    score_threshold: number;
    semantic_boost: boolean;
    user_ratio_boost: boolean;
    logic_type: string;
}

export interface ProfilingStats {
    activeUsers: number;
    dailyRows: number;
    summaryCount: number;
    summaryUsers: number;
}

export interface StatsReport {
    metrics: Record<string, number>;
    profiling: ProfilingStats;
    wordBank: WordBankStats;
    semantic: { available: boolean; model?: string; categories?: Record<string, number> };
    aiAvailable: boolean;
    detectorCount: number;
}

export interface SpotCheckEntry {
    requestId?: string | null;
    userId?: string | null;
    verdict?: string | null;
    suspicionScore?: number;
    matchedWord?: string | null;
    levelUsed?: number;
    aiTriggered?: boolean;
    timestamp?: string | null;
}

export interface TuneReport {
    status: string;
    feedbackWindow?: number;
    decisionWindow?: number;
    precision?: number;
    scoreThreshold?: number;
    weights?: Record<string, number>;
}
