import { ReactElement } from "react";
import {
    Card,
    Collapse,
    Descriptions,
    List,
    Progress,
    Space,
    Steps,
    Table,
    TableProps,
    Tag,
    Typography,
} from "antd";
import {
    CheckCircleOutlined,
    ClockCircleOutlined,
    CloseCircleOutlined,
    DislikeOutlined,
    LikeOutlined,
    LoadingOutlined,
    UserOutlined,
} from "@ant-design/icons";
import {
    DetectorRunTrace,
    ModerateDetailResult,
    PipelineTrace,
    Stage1Trace,
    Stage2Trace,
    Stage3Trace,
    StreamEvent,
} from "../../types";

interface DerivedPipeline {
    stage1: Stage1Trace | null;
    detectors: DetectorRunTrace[];
    stage2: Stage2Trace | null;
    stage3: Stage3Trace | null;
    trace: PipelineTrace | null;
    currentStep: number;
}

function lastOf(events: StreamEvent[], name: string): Record<string, unknown> | null {
    for (let index = events.length - 1; index >= 0; index--) {
        if (events[index].name === name) {
            return events[index].data;
        }
    }
    return null;
}

function derive(events: StreamEvent[], result: ModerateDetailResult | null): DerivedPipeline {
    const trace: PipelineTrace | null = result?.trace ?? null;
    const stage1Event: Record<string, unknown> | null = lastOf(events, "stage1_complete");
    const stage2Event: Record<string, unknown> | null = lastOf(events, "stage2_complete");
    const stage3Event: Record<string, unknown> | null = lastOf(events, "stage3_complete");
    const detectorEvents: Record<string, unknown>[] = events
        .filter((event) => event.name === "detector_result")
        .map((event) => event.data);

    const stage1: Stage1Trace | null = trace
        ? trace.stage_1
        : stage1Event
          ? {
                fast_path: Boolean(stage1Event.fast_path),
                verdict: String(stage1Event.verdict ?? ""),
                latency_ms: Number(stage1Event.latency_ms ?? 0),
            }
          : null;

    const detectors: DetectorRunTrace[] = trace
        ? trace.stage_2.detector_results
        : detectorEvents.map((data) => ({
              name: String(data.name),
              enabled: true,
              available: true,
              matched: Boolean(data.matched),
              blocking: Boolean(data.blocking),
              confidence: data.confidence != null ? Number(data.confidence) : null,
              matched_words: Array.isArray(data.matched_words)
                  ? (data.matched_words as string[])
                  : [],
              reason: data.reason != null ? String(data.reason) : null,
              latency_ms: Number(data.latency_ms ?? 0),
              weight: 0,
          }));

    const stage2: Stage2Trace | null = trace
        ? trace.stage_2
        : stage2Event
          ? {
                detector_results: [],
                semantic_similarities:
                    stage2Event.semantic_similarities != null
                        ? (stage2Event.semantic_similarities as Record<string, number>)
                        : {},
                semantic_enabled: Boolean(stage2Event.semantic_enabled),
                user_profile: stage2Event.user_profile
                    ? (stage2Event.user_profile as Stage2Trace["user_profile"])
                    : null,
                suspicion_score: Number(stage2Event.suspicion_score ?? 0),
                weight_contributions: Array.isArray(stage2Event.weight_contributions)
                    ? (stage2Event.weight_contributions as Stage2Trace["weight_contributions"])
                    : [],
                latency_ms: Number(stage2Event.latency_ms ?? 0),
            }
          : null;

    const stage3: Stage3Trace | null = trace
        ? (trace.stage_3 ?? null)
        : stage3Event
          ? {
                invoked: Boolean(stage3Event.invoked),
                trigger: stage3Event.trigger != null ? String(stage3Event.trigger) : null,
                model_available: Boolean(stage3Event.model_available),
                prompt: stage3Event.prompt != null ? String(stage3Event.prompt) : null,
                response: stage3Event.response != null ? String(stage3Event.response) : null,
                verdict: stage3Event.verdict != null ? String(stage3Event.verdict) : null,
                confidence: stage3Event.confidence != null ? Number(stage3Event.confidence) : null,
                latency_ms: Number(stage3Event.latency_ms ?? 0),
            }
          : null;

    let currentStep: number = 0;
    if (stage1 !== null) {
        currentStep = 1;
    }
    if (stage2 !== null) {
        currentStep = 2;
    }
    if (stage3 !== null || trace !== null) {
        currentStep = 3;
    }
    return { stage1, detectors, stage2, stage3, trace, currentStep };
}

function verdictColor(verdict: string | null): string {
    if (verdict === "BLOCK") {
        return "red";
    }
    if (verdict === "REVIEW") {
        return "orange";
    }
    return "green";
}

function scoreColor(score: number): string {
    if (score >= 60) {
        return "#dc2626";
    }
    if (score >= 30) {
        return "#d97706";
    }
    return "#16a34a";
}

function DetectorStatus(props: { run: DetectorRunTrace }): ReactElement {
    const { run } = props;
    if (!run.available) {
        return <Tag>Unavailable</Tag>;
    }
    if (!run.enabled) {
        return <Tag color="default">Disabled</Tag>;
    }
    if (run.matched) {
        return (
            <Tag color={run.blocking ? "red" : "orange"}>{run.blocking ? "BLOCK" : "REVIEW"}</Tag>
        );
    }
    return <Tag color="green">Clean</Tag>;
}

function SemanticPanel(props: {
    similarities: Record<string, number>;
    enabled: boolean;
}): ReactElement {
    const { similarities, enabled } = props;
    const entries: [string, number][] = Object.entries(similarities).sort((a, b) => b[1] - a[1]);
    if (!enabled) {
        return <Typography.Text type="secondary">Semantic similarity is disabled.</Typography.Text>;
    }
    if (entries.length === 0) {
        return <Typography.Text type="secondary">No similarity results returned.</Typography.Text>;
    }
    return (
        <Space direction="vertical" style={{ width: "100%" }} size="small">
            {entries.map(([category, value]) => (
                <Space key={category} style={{ width: "100%" }} align="center">
                    <Typography.Text style={{ width: 90 }}>{category}</Typography.Text>
                    <Progress
                        percent={Number((value * 100).toFixed(1))}
                        size="small"
                        strokeColor={value >= 0.85 ? "#dc2626" : "#2563eb"}
                        style={{ flex: 1 }}
                    />
                </Space>
            ))}
        </Space>
    );
}

function ContributionsPanel(props: {
    contributions: Stage2Trace["weight_contributions"];
}): ReactElement {
    const { contributions } = props;
    if (contributions.length === 0) {
        return (
            <Typography.Text type="secondary">
                No contributions to the suspicion score.
            </Typography.Text>
        );
    }
    return (
        <List
            size="small"
            dataSource={contributions}
            renderItem={(item) => (
                <List.Item>
                    <Space>
                        <Tag
                            color={
                                item.kind === "detector"
                                    ? "blue"
                                    : item.kind === "semantic"
                                      ? "purple"
                                      : "cyan"
                            }
                        >
                            {item.kind}
                        </Tag>
                        <Typography.Text>{item.name}</Typography.Text>
                        {item.kind === "detector" && (
                            <Typography.Text type="secondary">hit</Typography.Text>
                        )}
                        {item.kind === "semantic" && (
                            <Typography.Text type="secondary">
                                similarity {item.value}
                            </Typography.Text>
                        )}
                        {item.kind === "user" && (
                            <Typography.Text type="secondary">ratio {item.value}</Typography.Text>
                        )}
                        <Typography.Text type="secondary">weight {item.weight}</Typography.Text>
                    </Space>
                    <Typography.Text strong>+{item.contributed}</Typography.Text>
                </List.Item>
            )}
        />
    );
}

function Stage1Card(props: { stage1: Stage1Trace | null; running: boolean }): ReactElement {
    const { stage1, running } = props;
    if (stage1 === null) {
        return (
            <Card size="small" title="Stage 1 - Fast Path">
                {running ? (
                    <LoadingOutlined />
                ) : (
                    <Typography.Text type="secondary">Waiting for a request.</Typography.Text>
                )}
            </Card>
        );
    }
    return (
        <Card size="small" title="Stage 1 - Fast Path">
            <Space direction="vertical" style={{ width: "100%" }}>
                {stage1.fast_path ? (
                    <Space>
                        <CheckCircleOutlined style={{ color: "#16a34a" }} />
                        <Typography.Text strong>
                            Exited on the safe word list with PASS in {stage1.latency_ms.toFixed(2)}{" "}
                            ms
                        </Typography.Text>
                    </Space>
                ) : (
                    <Space>
                        <CloseCircleOutlined style={{ color: "#d97706" }} />
                        <Typography.Text>
                            Not a safe word match; continued to Stage 2.
                        </Typography.Text>
                    </Space>
                )}
                <Descriptions size="small" column={2}>
                    <Descriptions.Item label="Fast Path">
                        {stage1.fast_path ? "Yes" : "No"}
                    </Descriptions.Item>
                    <Descriptions.Item label="Verdict">
                        <Tag color={verdictColor(stage1.verdict)}>{stage1.verdict}</Tag>
                    </Descriptions.Item>
                    <Descriptions.Item label="Latency">
                        {stage1.latency_ms.toFixed(2)} ms
                    </Descriptions.Item>
                </Descriptions>
            </Space>
        </Card>
    );
}

function Stage2Card(props: {
    stage2: Stage2Trace | null;
    detectors: DetectorRunTrace[];
    running: boolean;
}): ReactElement {
    const { stage2, detectors, running } = props;
    if (stage2 === null) {
        return (
            <Card size="small" title="Stage 2 - Detectors &amp; Scoring">
                {running ? (
                    <LoadingOutlined />
                ) : (
                    <Typography.Text type="secondary">Waiting.</Typography.Text>
                )}
            </Card>
        );
    }
    const columns: TableProps<DetectorRunTrace>["columns"] = [
        { title: "Detector", dataIndex: "name", key: "name" },
        { title: "Status", key: "status", render: (_, run) => <DetectorStatus run={run} /> },
        {
            title: "Latency (ms)",
            dataIndex: "latency_ms",
            key: "latency_ms",
            render: (value: number) => value.toFixed(2),
        },
        { title: "Weight", dataIndex: "weight", key: "weight" },
        {
            title: "Confidence",
            dataIndex: "confidence",
            key: "confidence",
            render: (value: number | null) => (value != null ? value.toFixed(2) : "-"),
        },
        {
            title: "Detail",
            key: "detail",
            render: (_, run) => {
                if (run.matched) {
                    return (
                        <Space direction="vertical" size={0}>
                            {run.matched_words.length > 0 && (
                                <Typography.Text type="secondary">
                                    words: {run.matched_words.join(", ")}
                                </Typography.Text>
                            )}
                            <Typography.Text type="secondary">{run.reason}</Typography.Text>
                        </Space>
                    );
                }
                return <Typography.Text type="secondary">-</Typography.Text>;
            },
        },
    ];
    return (
        <Card size="small" title="Stage 2 - Detectors &amp; Scoring">
            <Space direction="vertical" style={{ width: "100%" }} size="middle">
                <Table<DetectorRunTrace>
                    rowKey="name"
                    size="small"
                    columns={columns}
                    dataSource={detectors}
                    pagination={false}
                />
                <Collapse
                    size="small"
                    items={[
                        {
                            key: "semantic",
                            label: `Semantic Similarity (${stage2.semantic_enabled ? "enabled" : "disabled"})`,
                            children: (
                                <SemanticPanel
                                    similarities={stage2.semantic_similarities}
                                    enabled={stage2.semantic_enabled}
                                />
                            ),
                        },
                        {
                            key: "contributions",
                            label: `Suspicion Score Breakdown (${stage2.suspicion_score.toFixed(1)})`,
                            children: (
                                <ContributionsPanel contributions={stage2.weight_contributions} />
                            ),
                        },
                    ]}
                />
                {stage2.user_profile !== null && stage2.user_profile !== undefined && (
                    <Descriptions size="small" column={2} title="User Profile">
                        <Descriptions.Item label="Bad Ratio">
                            {stage2.user_profile.ratio.toFixed(3)}
                        </Descriptions.Item>
                        <Descriptions.Item label="User ID">
                            {stage2.user_profile.user_id}
                        </Descriptions.Item>
                    </Descriptions>
                )}
                <Typography.Text type="secondary">
                    Stage latency: {stage2.latency_ms.toFixed(2)} ms
                </Typography.Text>
            </Space>
        </Card>
    );
}

function Stage3Card(props: { stage3: Stage3Trace | null; running: boolean }): ReactElement {
    const { stage3, running } = props;
    if (stage3 === null) {
        return (
            <Card size="small" title="Stage 3 - LLM">
                {running ? (
                    <LoadingOutlined />
                ) : (
                    <Typography.Text type="secondary">Waiting.</Typography.Text>
                )}
            </Card>
        );
    }
    if (!stage3.invoked) {
        return (
            <Card size="small" title="Stage 3 - LLM">
                <Space>
                    <DislikeOutlined style={{ color: "#16a34a" }} />
                    <Typography.Text>LLM was not invoked for this request.</Typography.Text>
                </Space>
            </Card>
        );
    }
    return (
        <Card size="small" title="Stage 3 - LLM">
            <Space direction="vertical" style={{ width: "100%" }} size="middle">
                <Descriptions size="small" column={2}>
                    <Descriptions.Item label="Trigger">{stage3.trigger}</Descriptions.Item>
                    <Descriptions.Item label="Model">
                        {stage3.model_available ? (
                            <Tag color="green">Available</Tag>
                        ) : (
                            <Tag color="red">Unavailable</Tag>
                        )}
                    </Descriptions.Item>
                    <Descriptions.Item label="Model Verdict">
                        {stage3.verdict === "BLOCK" ? (
                            <Tag color="red" icon={<CloseCircleOutlined />}>
                                BLOCK
                            </Tag>
                        ) : (
                            <Tag color="green" icon={<LikeOutlined />}>
                                ALLOW
                            </Tag>
                        )}
                    </Descriptions.Item>
                    <Descriptions.Item label="Confidence">
                        {stage3.confidence != null ? stage3.confidence.toFixed(2) : "-"}
                    </Descriptions.Item>
                    <Descriptions.Item label="Latency">
                        {stage3.latency_ms.toFixed(2)} ms
                    </Descriptions.Item>
                </Descriptions>
                <Collapse
                    size="small"
                    items={[
                        {
                            key: "prompt",
                            label: "Prompt",
                            children: <pre className="workbench-pre">{stage3.prompt}</pre>,
                        },
                        {
                            key: "response",
                            label: "Model Response",
                            children: <pre className="workbench-pre">{stage3.response}</pre>,
                        },
                    ]}
                />
            </Space>
        </Card>
    );
}

export function PipelineVisualization(props: {
    events: StreamEvent[];
    result: ModerateDetailResult | null;
    running: boolean;
}): ReactElement {
    const { events, result, running } = props;
    const derived: DerivedPipeline = derive(events, result);
    const verdict: string | null = derived.trace?.verdict ?? null;
    const score: number = derived.trace?.suspicion_score ?? derived.stage2?.suspicion_score ?? 0;
    const totalLatency: number = derived.trace?.total_latency_ms ?? 0;

    return (
        <Space direction="vertical" style={{ width: "100%" }} size="middle">
            <Steps
                size="small"
                current={derived.currentStep}
                status={derived.trace !== null ? "finish" : "process"}
                items={[{ title: "Fast Path" }, { title: "Detectors" }, { title: "LLM" }]}
            />
            <Space align="start" size="middle" className="workbench-result">
                <Progress
                    type="dashboard"
                    percent={score}
                    strokeColor={scoreColor(score)}
                    format={(percent) => `${percent?.toFixed(0) ?? 0}`}
                />
                <Space direction="vertical">
                    <Space>
                        <Typography.Text type="secondary">Verdict</Typography.Text>
                        {verdict !== null ? (
                            <Tag color={verdictColor(verdict)} className="workbench-verdict">
                                {verdict}
                            </Tag>
                        ) : (
                            <Tag>Pending</Tag>
                        )}
                    </Space>
                    <Space>
                        <Typography.Text type="secondary">Total latency</Typography.Text>
                        <Typography.Text strong>{totalLatency.toFixed(2)} ms</Typography.Text>
                    </Space>
                    <Space>
                        <Typography.Text type="secondary">Level used</Typography.Text>
                        <Typography.Text strong>{derived.trace?.level_used ?? "-"}</Typography.Text>
                    </Space>
                    {derived.trace !== null && derived.trace.reasons.length > 0 && (
                        <Space wrap>
                            <Typography.Text type="secondary">Reasons</Typography.Text>
                            {derived.trace.reasons.map((reason) => (
                                <Tag key={reason}>{reason}</Tag>
                            ))}
                        </Space>
                    )}
                    {derived.trace !== null && derived.trace.user_id && (
                        <Space>
                            <UserOutlined />
                            <Typography.Text type="secondary">
                                {derived.trace.user_id}
                            </Typography.Text>
                        </Space>
                    )}
                </Space>
            </Space>
            {!running && derived.trace === null && events.length === 0 && (
                <Typography.Text type="secondary">
                    Paste a message in the panel above and press Moderate to trace the pipeline.
                </Typography.Text>
            )}
            {running && (
                <Space>
                    <ClockCircleOutlined style={{ color: "#2563eb" }} />
                    <Typography.Text type="secondary">Pipeline running...</Typography.Text>
                </Space>
            )}
            <Stage1Card stage1={derived.stage1} running={running} />
            <Stage2Card stage2={derived.stage2} detectors={derived.detectors} running={running} />
            <Stage3Card stage3={derived.stage3} running={running} />
        </Space>
    );
}
