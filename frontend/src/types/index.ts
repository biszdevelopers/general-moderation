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

export interface AuditEntry {
    timestamp?: string;
    level?: string;
    message?: string;
    requestId?: string | null;
    userId?: string | null;
    textHash?: string;
    textPreview?: string;
    verdict?: string | null;
    levelUsed?: number;
    reason?: string | null;
    matchedWord?: string | null;
    matchedLanguage?: string | null;
    confidenceScore?: number | null;
    latencyMs?: number;
    detectorChain?: string[];
    suspicionScore?: number;
    aiTriggered?: boolean;
}

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

export interface PhraseEntry {
    id: number;
    phrase: string;
    language: string;
    category: string;
    severity: number;
    created_at: string;
}

export interface PhrasePayload {
    phrase: string;
    language: string;
    category: string;
    severity: number;
}

export interface SemanticStatus {
    available: boolean;
    ready: boolean;
    loading: boolean;
    model?: string;
    categories: Record<string, number>;
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

export interface DetectorRunTrace {
    name: string;
    enabled: boolean;
    available: boolean;
    matched: boolean;
    blocking: boolean;
    confidence?: number | null;
    matched_words: string[];
    matched_language?: string | null;
    reason?: string | null;
    latency_ms: number;
    weight: number;
}

export interface Stage1Trace {
    fast_path: boolean;
    verdict: string;
    latency_ms: number;
}

export interface WeightContribution {
    kind: "detector" | "semantic" | "user";
    name: string;
    value: number;
    weight: number;
    contributed: number;
}

export interface Stage2Trace {
    detector_results: DetectorRunTrace[];
    semantic_similarities: Record<string, number>;
    semantic_enabled: boolean;
    user_profile?: {
        app_name: string;
        user_id: string;
        ratio: number;
        daily: unknown[];
        summaries: unknown[];
    } | null;
    suspicion_score: number;
    weight_contributions: WeightContribution[];
    latency_ms: number;
}

export interface Stage3Trace {
    invoked: boolean;
    trigger?: string | null;
    model_available: boolean;
    prompt?: string | null;
    response?: string | null;
    verdict?: string | null;
    confidence?: number | null;
    latency_ms: number;
}

export interface PipelineTrace {
    request_id?: string | null;
    app_name: string;
    user_id?: string | null;
    text: string;
    verdict: Verdict;
    suspicion_score: number;
    level_used: number;
    ai_triggered: boolean;
    reasons: string[];
    matched_words: string[];
    matched_language?: string | null;
    confidence_score?: number | null;
    stage_1: Stage1Trace;
    stage_2: Stage2Trace;
    stage_3?: Stage3Trace | null;
    total_latency_ms: number;
}

export interface ModerateDetailResult {
    response: ModerationResponse;
    trace: PipelineTrace;
}

export interface ModerateDetailRequest {
    text: string;
    user_id?: string;
    app_name?: string;
}

export interface StreamEvent {
    name: string;
    data: Record<string, unknown>;
}

export type TextSource = "random" | "corpus" | "custom";

export interface LoadTestConfig {
    concurrent_users: number;
    requests_per_user: number;
    text_source: TextSource;
    corpus: string[];
    custom_texts: string[];
    app_name: string;
    user_prefix: string;
}

export interface LoadTestProgress {
    completed: number;
    total: number;
    elapsed_ms: number;
    rps: number;
    p50: number;
    p95: number;
    p99: number;
    errors: number;
    llm_invocations: number;
    verdicts: Record<string, number>;
}

export interface LoadTestResult {
    total_requests: number;
    successful_requests: number;
    failed_requests: number;
    total_duration_ms: number;
    requests_per_second: number;
    latency_percentiles: Record<string, number>;
    max_concurrency_reached: number;
    llm_invocation_count: number;
    error_distribution: Record<string, number>;
    verdicts: Record<string, number>;
}

export interface DashboardReport {
    total_requests_today: number;
    blocked_today: number;
    block_rate: number;
    avg_latency_ms: number;
    llm_invocations_today: number;
    llm_invocation_rate: number;
    top_detectors: { name: string; count: number }[];
    requests_over_time: { bucket: string; count: number }[];
    metrics: Record<string, number>;
}

export interface UserDailyRow {
    day_offset: number;
    total_msgs: number;
    flagged_msgs: number;
    blocked_msgs: number;
    reviewed_msgs: number;
    date: string;
}

export interface UserSummary {
    cycle_id: number;
    start_day: string;
    end_day: string;
    total_msgs: number;
    flagged_msgs: number;
    blocked_msgs: number;
    reviewed_msgs: number;
    next_cycle_id?: number | null;
}

export interface UserProfile {
    app_name: string;
    user_id: string;
    daily: UserDailyRow[];
    summaries: UserSummary[];
    ratio: number;
    total_msgs: number;
    flagged_msgs: number;
    blocked_msgs: number;
}
