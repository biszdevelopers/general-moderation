import { ReactElement, useEffect, useState } from "react";
import {
    App as AntdApp,
    Button,
    Card,
    Col,
    List,
    Progress,
    Row,
    Space,
    Statistic,
    Tag,
    Tooltip,
    Typography,
} from "antd";
import { ReloadOutlined } from "@ant-design/icons";
import { useAppContext } from "../../contexts/AppContext";
import { DashboardReport } from "../../types";

function RequestsChart(props: { buckets: { bucket: string; count: number }[] }): ReactElement {
    const { buckets } = props;
    if (buckets.length === 0) {
        return (
            <Typography.Text type="secondary">
                No moderation requests recorded today.
            </Typography.Text>
        );
    }
    const maxCount: number = Math.max(1, ...buckets.map((bucket) => bucket.count));
    return (
        <div className="ratio-chart">
            {buckets.map((bucket) => {
                const height: number = Math.max(2, (bucket.count / maxCount) * 90);
                return (
                    <Tooltip
                        key={bucket.bucket}
                        title={`${bucket.bucket}: ${bucket.count} requests`}
                    >
                        <div className="ratio-chart__col" style={{ height: "100%" }}>
                            <div
                                className="ratio-chart__bar"
                                style={{ height: `${height}%`, backgroundColor: "#2563eb" }}
                            />
                            <div className="ratio-chart__label">{bucket.bucket}</div>
                        </div>
                    </Tooltip>
                );
            })}
        </div>
    );
}

export function DashboardPanel(): ReactElement {
    const { testApiService } = useAppContext();
    const { message } = AntdApp.useApp();
    const [report, setReport] = useState<DashboardReport | null>(null);
    const [loading, setLoading] = useState<boolean>(false);

    const load = async (): Promise<void> => {
        setLoading(true);
        try {
            setReport(await testApiService.getDashboard());
        } catch (err: unknown) {
            message.error(`Failed to load dashboard: ${String(err)}`);
        } finally {
            setLoading(false);
        }
    };

    useEffect(() => {
        void load();
        const timer: ReturnType<typeof setInterval> = setInterval(() => {
            void load();
        }, 5000);
        return () => clearInterval(timer);
    }, []);

    return (
        <Card
            title="Real-Time Dashboard"
            className="workbench-card"
            extra={
                <Space>
                    <Typography.Text type="secondary">
                        Auto-refreshes every 5 seconds
                    </Typography.Text>
                    <Button icon={<ReloadOutlined />} loading={loading} onClick={() => void load()}>
                        Refresh
                    </Button>
                </Space>
            }
        >
            {report === null ? (
                <Typography.Text type="secondary">Loading dashboard metrics...</Typography.Text>
            ) : (
                <Space direction="vertical" style={{ width: "100%" }} size="large">
                    <Row gutter={[16, 16]}>
                        <Col xs={12} md={6}>
                            <Statistic title="Requests Today" value={report.total_requests_today} />
                        </Col>
                        <Col xs={12} md={6}>
                            <Statistic
                                title="Block Rate"
                                value={report.block_rate * 100}
                                precision={1}
                                suffix="%"
                            />
                        </Col>
                        <Col xs={12} md={6}>
                            <Statistic
                                title="Avg Latency (ms)"
                                value={report.avg_latency_ms}
                                precision={2}
                            />
                        </Col>
                        <Col xs={12} md={6}>
                            <Statistic
                                title="LLM Invocation Rate"
                                value={report.llm_invocation_rate * 100}
                                precision={1}
                                suffix="%"
                            />
                        </Col>
                    </Row>
                    <Card size="small" title="Requests Over Time (today)">
                        <RequestsChart buckets={report.requests_over_time} />
                    </Card>
                    <Row gutter={[16, 16]}>
                        <Col xs={24} md={12}>
                            <Card size="small" title="Most Frequent Detectors">
                                {report.top_detectors.length === 0 ? (
                                    <Typography.Text type="secondary">
                                        No detector activity yet.
                                    </Typography.Text>
                                ) : (
                                    <List
                                        size="small"
                                        dataSource={report.top_detectors}
                                        renderItem={(item) => (
                                            <List.Item>
                                                <Space style={{ width: "100%" }}>
                                                    <Tag color="blue">{item.name}</Tag>
                                                    <Progress
                                                        percent={Math.round(
                                                            (item.count /
                                                                Math.max(
                                                                    1,
                                                                    report.top_detectors[0].count,
                                                                )) *
                                                                100,
                                                        )}
                                                        size="small"
                                                        style={{ flex: 1 }}
                                                    />
                                                    <Typography.Text>{item.count}</Typography.Text>
                                                </Space>
                                            </List.Item>
                                        )}
                                    />
                                )}
                            </Card>
                        </Col>
                        <Col xs={24} md={12}>
                            <Card size="small" title="Engine Counters">
                                <List
                                    size="small"
                                    dataSource={Object.entries(report.metrics)}
                                    renderItem={([name, value]) => (
                                        <List.Item>
                                            <Typography.Text>{name}</Typography.Text>
                                            <Typography.Text strong>{value}</Typography.Text>
                                        </List.Item>
                                    )}
                                />
                            </Card>
                        </Col>
                    </Row>
                </Space>
            )}
        </Card>
    );
}
