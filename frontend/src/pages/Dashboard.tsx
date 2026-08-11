import { App as AntdApp, Card, Col, Row, Space, Table, Tag, Typography } from "antd";
import { TableProps } from "antd";
import { useEffect, useState } from "react";
import { ReactElement } from "react";
import { useAppContext } from "../contexts/AppContext";
import { AuditEntry, HealthReport, WordBankStats } from "../types";
import { LoadingSpinner } from "../components/LoadingSpinner";
import { StatsCard } from "../components/StatsCard";

function verdictTag(value: unknown): ReactElement {
    const verdict: string = String(value ?? "");
    const color: string = verdict === "BLOCK" ? "red" : verdict === "REVIEW" ? "orange" : "green";
    return <Tag color={color}>{verdict || "-"}</Tag>;
}

export function Dashboard(): ReactElement {
    const { settingsService, wordBankService, auditService } = useAppContext();
    const { message } = AntdApp.useApp();
    const [health, setHealth] = useState<HealthReport | null>(null);
    const [stats, setStats] = useState<WordBankStats | null>(null);
    const [recent, setRecent] = useState<AuditEntry[]>([]);
    const [loading, setLoading] = useState<boolean>(true);

    useEffect(() => {
        const loadData = async (): Promise<void> => {
            try {
                const [healthReport, wordBankStats, entries] = await Promise.all([
                    settingsService.getHealth(),
                    wordBankService.getStats(),
                    auditService.getAudit(),
                ]);
                setHealth(healthReport);
                setStats(wordBankStats);
                setRecent(entries.slice(0, 10));
            } catch (error: unknown) {
                message.error(`Failed to load dashboard: ${String(error)}`);
            } finally {
                setLoading(false);
            }
        };
        void loadData();
    }, [settingsService, wordBankService, auditService, message]);

    const columns: TableProps<AuditEntry>["columns"] = [
        { title: "Timestamp", dataIndex: "timestamp", key: "timestamp" },
        { title: "Verdict", dataIndex: "verdict", key: "verdict", render: verdictTag },
        { title: "Level", dataIndex: "levelUsed", key: "levelUsed" },
        { title: "Matched Word", dataIndex: "matchedWord", key: "matchedWord" },
        { title: "Reason", dataIndex: "reason", key: "reason", ellipsis: true },
        {
            title: "Latency (ms)",
            dataIndex: "latencyMs",
            key: "latencyMs",
            render: (value: unknown): string => {
                const numeric: number = Number(value);
                return Number.isFinite(numeric) ? numeric.toFixed(2) : "-";
            },
        },
    ];

    if (loading) {
        return <LoadingSpinner />;
    }

    return (
        <div className="page">
            <Typography.Title level={2} className="page__title">
                Dashboard
            </Typography.Title>
            <Row gutter={[16, 16]} className="dashboard-grid">
                <Col xs={24} sm={12} lg={6}>
                    <StatsCard title="Total Words" value={stats?.totalWords ?? 0} />
                </Col>
                <Col xs={24} sm={12} lg={6}>
                    <StatsCard title="Custom Words" value={stats?.customWords ?? 0} />
                </Col>
                <Col xs={24} sm={12} lg={6}>
                    <StatsCard title="Base Words" value={stats?.baseWords ?? 0} />
                </Col>
                <Col xs={24} sm={12} lg={6}>
                    <StatsCard title="Languages" value={stats?.languages ?? 0} />
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
                            <div className="detector-list">
                                {health?.detectors.map((detector) => (
                                    <Space key={detector.name} className="detector-item">
                                        <Typography.Text>{detector.name}</Typography.Text>
                                        <Tag color={detector.available ? "green" : "default"}>
                                            {detector.available ? "Ready" : "Not installed"}
                                        </Tag>
                                    </Space>
                                ))}
                            </div>
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
                            locale={{ emptyText: "No moderation activity yet" }}
                        />
                    </Card>
                </Col>
            </Row>
        </div>
    );
}
