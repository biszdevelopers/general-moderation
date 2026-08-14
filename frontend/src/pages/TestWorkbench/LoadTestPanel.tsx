import { ReactElement, useState } from "react";
import {
    App as AntdApp,
    Button,
    Card,
    Col,
    Input,
    Progress,
    Radio,
    Row,
    Slider,
    Space,
    Statistic,
    Tag,
    Typography,
} from "antd";
import { DownloadOutlined, PlayCircleOutlined } from "@ant-design/icons";
import { useAppContext } from "../../contexts/AppContext";
import { useSseStream } from "../../hooks/useSseStream";
import { LoadTestConfig, LoadTestProgress, LoadTestResult, TextSource } from "../../types";

function download(filename: string, content: string, mime: string): void {
    const blob: Blob = new Blob([content], { type: mime });
    const url: string = URL.createObjectURL(blob);
    const anchor: HTMLAnchorElement = document.createElement("a");
    anchor.href = url;
    anchor.download = filename;
    anchor.click();
    URL.revokeObjectURL(url);
}

function latestOf(
    events: { name: string; data: Record<string, unknown> }[],
    name: string,
): Record<string, unknown> | null {
    for (let index = events.length - 1; index >= 0; index--) {
        if (events[index].name === name) {
            return events[index].data;
        }
    }
    return null;
}

function resultToCsv(result: LoadTestResult): string {
    const rows: [string, string | number][] = [
        ["total_requests", result.total_requests],
        ["successful_requests", result.successful_requests],
        ["failed_requests", result.failed_requests],
        ["total_duration_ms", result.total_duration_ms],
        ["requests_per_second", result.requests_per_second],
        ["max_concurrency_reached", result.max_concurrency_reached],
        ["llm_invocation_count", result.llm_invocation_count],
        ["p50_latency_ms", result.latency_percentiles.p50 ?? 0],
        ["p95_latency_ms", result.latency_percentiles.p95 ?? 0],
        ["p99_latency_ms", result.latency_percentiles.p99 ?? 0],
    ];
    return `metric,value\n${rows.map(([key, value]) => `${key},${value}`).join("\n")}\n`;
}

export function LoadTestPanel(): ReactElement {
    const { testApiService } = useAppContext();
    const { message } = AntdApp.useApp();
    const { running, events, error, start, reset } = useSseStream();
    const [concurrentUsers, setConcurrentUsers] = useState<number>(10);
    const [requestsPerUser, setRequestsPerUser] = useState<number>(10);
    const [textSource, setTextSource] = useState<TextSource>("random");
    const [corpusText, setCorpusText] = useState<string>(
        "hello world\nI will kill you tonight\nthanks for the update",
    );
    const [result, setResult] = useState<LoadTestResult | null>(null);

    const progress: LoadTestProgress | null = (() => {
        const data: Record<string, unknown> | null = latestOf(events, "progress");
        if (data === null) {
            return null;
        }
        return data as unknown as LoadTestProgress;
    })();
    const completed: number = progress?.completed ?? 0;
    const total: number = progress?.total ?? concurrentUsers * requestsPerUser;
    const percent: number = total > 0 ? Math.round((completed / total) * 100) : 0;

    const onRun = async (): Promise<void> => {
        setResult(null);
        reset();
        const lines: string[] = corpusText
            .split("\n")
            .map((line) => line.trim())
            .filter((line) => line.length > 0);
        const config: LoadTestConfig = {
            concurrent_users: concurrentUsers,
            requests_per_user: requestsPerUser,
            text_source: textSource,
            corpus: lines,
            custom_texts: lines,
            app_name: "default",
            user_prefix: "loadtest",
        };
        const streamResult = await start((onEvent) => testApiService.runLoadTest(config, onEvent));
        if (streamResult !== null) {
            setResult(streamResult as LoadTestResult);
            message.success("Load test complete");
        }
    };

    const onExport = (format: "csv" | "json"): void => {
        if (result === null) {
            return;
        }
        if (format === "csv") {
            download("load-test.csv", resultToCsv(result), "text/csv");
        } else {
            download("load-test.json", JSON.stringify(result, null, 2), "application/json");
        }
    };

    return (
        <Card title="Load Test" className="workbench-card">
            <Space direction="vertical" style={{ width: "100%" }} size="large">
                <Row gutter={[24, 16]}>
                    <Col xs={24} md={8}>
                        <Typography.Text>Concurrent users: {concurrentUsers}</Typography.Text>
                        <Slider
                            min={1}
                            max={1000}
                            value={concurrentUsers}
                            onChange={(value) => setConcurrentUsers(value)}
                            disabled={running}
                        />
                    </Col>
                    <Col xs={24} md={8}>
                        <Typography.Text>Requests per user: {requestsPerUser}</Typography.Text>
                        <Slider
                            min={1}
                            max={100}
                            value={requestsPerUser}
                            onChange={(value) => setRequestsPerUser(value)}
                            disabled={running}
                        />
                    </Col>
                    <Col xs={24} md={8}>
                        <Radio.Group
                            value={textSource}
                            onChange={(event) => setTextSource(event.target.value as TextSource)}
                            disabled={running}
                        >
                            <Radio.Button value="random">Random</Radio.Button>
                            <Radio.Button value="corpus">Corpus</Radio.Button>
                            <Radio.Button value="custom">Custom</Radio.Button>
                        </Radio.Group>
                    </Col>
                </Row>
                {textSource !== "random" && (
                    <Input.TextArea
                        rows={4}
                        value={corpusText}
                        onChange={(event) => setCorpusText(event.target.value)}
                        disabled={running}
                        placeholder="One message per line"
                    />
                )}
                <Button
                    type="primary"
                    icon={<PlayCircleOutlined />}
                    loading={running}
                    onClick={() => void onRun()}
                >
                    {running ? "Running..." : "Run Load Test"}
                </Button>
                {error !== null && <Typography.Text type="danger">{error}</Typography.Text>}
                {running && (
                    <Space direction="vertical" style={{ width: "100%" }}>
                        <Progress percent={percent} status="active" />
                        <Row gutter={[16, 16]}>
                            <Col span={6}>
                                <Statistic
                                    title="Completed"
                                    value={completed}
                                    suffix={`/ ${total}`}
                                />
                            </Col>
                            <Col span={6}>
                                <Statistic title="RPS" value={progress?.rps ?? 0} precision={2} />
                            </Col>
                            <Col span={6}>
                                <Statistic
                                    title="p50 / p95 / p99 (ms)"
                                    value={`${progress?.p50 ?? "-"} / ${progress?.p95 ?? "-"} / ${progress?.p99 ?? "-"}`}
                                />
                            </Col>
                            <Col span={6}>
                                <Statistic
                                    title="LLM invocations"
                                    value={progress?.llm_invocations ?? 0}
                                />
                            </Col>
                        </Row>
                    </Space>
                )}
                {result !== null && (
                    <Space direction="vertical" style={{ width: "100%" }} size="middle">
                        <Row gutter={[16, 16]}>
                            <Col xs={12} md={4}>
                                <Statistic title="Total Requests" value={result.total_requests} />
                            </Col>
                            <Col xs={12} md={4}>
                                <Statistic
                                    title="Requests / Second"
                                    value={result.requests_per_second}
                                    precision={2}
                                />
                            </Col>
                            <Col xs={12} md={4}>
                                <Statistic
                                    title="p50 (ms)"
                                    value={result.latency_percentiles.p50 ?? 0}
                                    precision={2}
                                />
                            </Col>
                            <Col xs={12} md={4}>
                                <Statistic
                                    title="p95 (ms)"
                                    value={result.latency_percentiles.p95 ?? 0}
                                    precision={2}
                                />
                            </Col>
                            <Col xs={12} md={4}>
                                <Statistic
                                    title="p99 (ms)"
                                    value={result.latency_percentiles.p99 ?? 0}
                                    precision={2}
                                />
                            </Col>
                        </Row>
                        <Row gutter={[16, 16]}>
                            <Col xs={12} md={4}>
                                <Statistic title="Failed" value={result.failed_requests} />
                            </Col>
                            <Col xs={12} md={4}>
                                <Statistic
                                    title="Max Concurrency"
                                    value={result.max_concurrency_reached}
                                />
                            </Col>
                            <Col xs={12} md={4}>
                                <Statistic
                                    title="LLM Invocations"
                                    value={result.llm_invocation_count}
                                />
                            </Col>
                            <Col xs={12} md={4}>
                                <Statistic
                                    title="Duration (s)"
                                    value={result.total_duration_ms / 1000}
                                    precision={2}
                                />
                            </Col>
                        </Row>
                        <Space wrap>
                            {Object.entries(result.verdicts).map(([verdict, count]) => (
                                <Tag
                                    key={verdict}
                                    color={
                                        verdict === "BLOCK"
                                            ? "red"
                                            : verdict === "REVIEW"
                                              ? "orange"
                                              : "green"
                                    }
                                >
                                    {verdict}: {count}
                                </Tag>
                            ))}
                        </Space>
                        <Space>
                            <Button icon={<DownloadOutlined />} onClick={() => onExport("csv")}>
                                Export CSV
                            </Button>
                            <Button icon={<DownloadOutlined />} onClick={() => onExport("json")}>
                                Export JSON
                            </Button>
                        </Space>
                    </Space>
                )}
            </Space>
        </Card>
    );
}
