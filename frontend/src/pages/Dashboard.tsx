import {
    App as AntdApp,
    Button,
    Card,
    Col,
    Empty,
    List,
    Row,
    Space,
    Statistic,
    Table,
    Tag,
    Typography,
} from "antd";
import { TableProps } from "antd";
import {
    AppstoreAddOutlined,
    BlockOutlined,
    DashboardOutlined,
    DatabaseOutlined,
    GlobalOutlined,
    ReloadOutlined,
    ThunderboltOutlined,
} from "@ant-design/icons";
import { useEffect, useState } from "react";
import { ReactElement } from "react";
import { useAppContext } from "../contexts/AppContext";
import { AuditEntry, DashboardReport, HealthReport, WordBankStats } from "../types";
import { LoadingSpinner } from "../components/LoadingSpinner";
import { LoginPrompt } from "../components/LoginPrompt";
import { StatsCard } from "../components/StatsCard";
import { BarChart, BarDatum } from "../components/BarChart";

function verdictTag(value: unknown): ReactElement {
    const verdict: string = String(value ?? "");
    const color: string = verdict === "BLOCK" ? "red" : verdict === "REVIEW" ? "orange" : "green";
    return <Tag color={color}>{verdict || "-"}</Tag>;
}

function latency(value: unknown): string {
    const numeric: number = Number(value);
    return Number.isFinite(numeric) ? numeric.toFixed(2) : "-";
}

export function Dashboard(): ReactElement {
    const { settingsService, wordBankService, auditService, testApiService, authenticated } =
        useAppContext();
    const { message } = AntdApp.useApp();
    const [report, setReport] = useState<DashboardReport | null>(null);
    const [health, setHealth] = useState<HealthReport | null>(null);
    const [stats, setStats] = useState<WordBankStats | null>(null);
    const [recent, setRecent] = useState<AuditEntry[]>([]);
    const [loading, setLoading] = useState<boolean>(true);
    const [refreshing, setRefreshing] = useState<boolean>(false);

    useEffect(() => {
        if (!authenticated) {
            setLoading(false);
            return;
        }
        const loadData = async (): Promise<void> => {
            try {
                const [reportResult, healthReport, wordBankStats, entries] = await Promise.all([
                    testApiService.getDashboard(),
                    settingsService.getHealth(),
                    wordBankService.getStats(),
                    auditService.getAudit(),
                ]);
                setReport(reportResult);
                setHealth(healthReport);
                setStats(wordBankStats);
                setRecent(entries.slice(0, 10));
            } catch (error: unknown) {
                if (report === null) {
                    message.error(`Failed to load dashboard: ${String(error)}`);
                }
            } finally {
                setLoading(false);
                setRefreshing(false);
            }
        };
        void loadData();
        const timer: ReturnType<typeof setInterval> = setInterval(() => {
            void loadData();
        }, 5000);
        return () => clearInterval(timer);
    }, [settingsService, wordBankService, auditService, testApiService, message, authenticated]);

    const onRefresh = async (): Promise<void> => {
        setRefreshing(true);
        try {
            const [reportResult, healthReport, wordBankStats, entries] = await Promise.all([
                testApiService.getDashboard(),
                settingsService.getHealth(),
                wordBankService.getStats(),
                auditService.getAudit(),
            ]);
            setReport(reportResult);
            setHealth(healthReport);
            setStats(wordBankStats);
            setRecent(entries.slice(0, 10));
        } catch (error: unknown) {
            message.error(`Refresh failed: ${String(error)}`);
        } finally {
            setRefreshing(false);
        }
    };

    const columns: TableProps<AuditEntry>["columns"] = [
        { title: "Timestamp", dataIndex: "timestamp", key: "timestamp" },
        { title: "Verdict", dataIndex: "verdict", key: "verdict", render: verdictTag },
        { title: "Level", dataIndex: "levelUsed", key: "levelUsed" },
        { title: "Matched Word", dataIndex: "matchedWord", key: "matchedWord" },
        { title: "Reason", dataIndex: "reason", key: "reason", ellipsis: true },
        { title: "Latency (ms)", dataIndex: "latencyMs", key: "latencyMs", render: latency },
    ];

    if (!authenticated) {
        return <LoginPrompt />;
    }

    if (loading) {
        return <LoadingSpinner />;
    }

    const overTime: BarDatum[] = (report?.requests_over_time ?? []).map((bucket) => ({
        label: bucket.bucket,
        value: bucket.count,
        hint: `${bucket.bucket}: ${bucket.count} request${bucket.count === 1 ? "" : "s"}`,
    }));
    const topDetectors: BarDatum[] = (report?.top_detectors ?? []).map((detector) => ({
        label: detector.name,
        value: detector.count,
        hint: `${detector.name}: ${detector.count}`,
        color: "#7c3aed",
    }));

    return (
        <div className="page">
            <Typography.Title level={2} className="page__title">
                Dashboard
            </Typography.Title>
            <Typography.Paragraph className="page__subtitle">
                Live overview of moderation traffic, detection pipeline, and recent activity.
                Auto-refreshes every 5 seconds.
            </Typography.Paragraph>
            <Row gutter={[16, 16]} className="dashboard-grid">
                <Col xs={24} sm={12} lg={6}>
                    <StatsCard
                        title="Total Words"
                        value={stats?.totalWords ?? 0}
                        icon={<DatabaseOutlined />}
                    />
                </Col>
                <Col xs={24} sm={12} lg={6}>
                    <StatsCard
                        title="Custom Words"
                        value={stats?.customWords ?? 0}
                        color="#7c3aed"
                        icon={<AppstoreAddOutlined />}
                    />
                </Col>
                <Col xs={24} sm={12} lg={6}>
                    <StatsCard
                        title="Base Words"
                        value={stats?.baseWords ?? 0}
                        color="#0ea5e9"
                        icon={<BlockOutlined />}
                    />
                </Col>
                <Col xs={24} sm={12} lg={6}>
                    <StatsCard
                        title="Languages"
                        value={stats?.languages ?? 0}
                        color="#16a34a"
                        icon={<GlobalOutlined />}
                    />
                </Col>
            </Row>
            <Card
                title="Live Traffic"
                className="dashboard-card"
                extra={
                    <Space>
                        <Typography.Text type="secondary">Auto-refresh 5s</Typography.Text>
                        <Button
                            icon={<ReloadOutlined />}
                            loading={refreshing}
                            onClick={() => void onRefresh()}
                        >
                            Refresh
                        </Button>
                    </Space>
                }
            >
                <Row gutter={[16, 16]}>
                    <Col xs={12} md={6}>
                        <Statistic
                            title="Requests Today"
                            value={report?.total_requests_today ?? 0}
                            prefix={<DashboardOutlined />}
                        />
                    </Col>
                    <Col xs={12} md={6}>
                        <Statistic
                            title="Block Rate"
                            value={(report?.block_rate ?? 0) * 100}
                            precision={1}
                            suffix="%"
                            valueStyle={{
                                color: (report?.block_rate ?? 0) > 0.3 ? "#dc2626" : undefined,
                            }}
                        />
                    </Col>
                    <Col xs={12} md={6}>
                        <Statistic
                            title="Avg Latency (ms)"
                            value={report?.avg_latency_ms ?? 0}
                            precision={2}
                        />
                    </Col>
                    <Col xs={12} md={6}>
                        <Statistic
                            title="LLM Invocation Rate"
                            value={(report?.llm_invocation_rate ?? 0) * 100}
                            precision={1}
                            suffix="%"
                            prefix={<ThunderboltOutlined />}
                        />
                    </Col>
                </Row>
            </Card>
            <Row gutter={[16, 16]}>
                <Col xs={24} lg={14}>
                    <Card title="Requests Over Time (today)" className="dashboard-card">
                        {overTime.length === 0 ? (
                            <Empty description="No moderation requests recorded today." />
                        ) : (
                            <BarChart data={overTime} />
                        )}
                    </Card>
                </Col>
                <Col xs={24} lg={10}>
                    <Card title="Most Frequent Detectors" className="dashboard-card">
                        {topDetectors.length === 0 ? (
                            <Empty description="No detector activity yet." />
                        ) : (
                            <BarChart data={topDetectors} height={140} />
                        )}
                    </Card>
                </Col>
            </Row>
            <Row gutter={[16, 16]}>
                <Col xs={24} lg={10}>
                    <Card title="Detector Status" className="dashboard-card">
                        <Space direction="vertical" size="middle" style={{ width: "100%" }}>
                            <Space>
                                <Typography.Text>Level 2 (llama.cpp):</Typography.Text>
                                <Tag color={health?.llamaAvailable === true ? "green" : "red"}>
                                    {health?.llamaAvailable === true ? "Available" : "Unavailable"}
                                </Tag>
                            </Space>
                            <List
                                size="small"
                                dataSource={health?.detectors ?? []}
                                locale={{ emptyText: "No detectors reported" }}
                                renderItem={(detector) => (
                                    <List.Item>
                                        <Typography.Text>{detector.name}</Typography.Text>
                                        <Tag color={detector.available ? "green" : "default"}>
                                            {detector.available ? "Ready" : "Not installed"}
                                        </Tag>
                                    </List.Item>
                                )}
                            />
                            {health !== null && (
                                <Typography.Text type="secondary">
                                    Uptime: {Math.round(health.uptimeSeconds)} seconds
                                </Typography.Text>
                            )}
                        </Space>
                    </Card>
                </Col>
                <Col xs={24} lg={14}>
                    <Card title="Recent Activity" className="dashboard-card">
                        <Table<AuditEntry>
                            rowKey={(entry: AuditEntry, index?: number): string =>
                                `${String(index ?? 0)}-${String(entry.timestamp ?? "")}`
                            }
                            columns={columns}
                            dataSource={recent}
                            pagination={false}
                            size="small"
                            scroll={{ x: "max-content" }}
                            locale={{ emptyText: "No moderation activity yet" }}
                        />
                    </Card>
                </Col>
            </Row>
        </div>
    );
}
