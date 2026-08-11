import { Card, Col, Row, Space, Tag, Typography, App as AntdApp } from "antd";
import { useEffect, useState } from "react";
import { ReactElement } from "react";
import { useAppContext } from "../contexts/AppContext";
import { HealthReport, WordBankStats } from "../types";
import { LoadingSpinner } from "../components/LoadingSpinner";
import { StatsCard } from "../components/StatsCard";

export function Dashboard(): ReactElement {
    const { settingsService, wordBankService } = useAppContext();
    const { message } = AntdApp.useApp();
    const [health, setHealth] = useState<HealthReport | null>(null);
    const [stats, setStats] = useState<WordBankStats | null>(null);
    const [loading, setLoading] = useState<boolean>(true);

    useEffect(() => {
        const loadData = async (): Promise<void> => {
            try {
                const [healthReport, wordBankStats] = await Promise.all([
                    settingsService.getHealth(),
                    wordBankService.getStats(),
                ]);
                setHealth(healthReport);
                setStats(wordBankStats);
            } catch (error: unknown) {
                message.error(`Failed to load dashboard: ${String(error)}`);
            } finally {
                setLoading(false);
            }
        };
        void loadData();
    }, [settingsService, wordBankService, message]);

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
            <Card title="Detector Status" className="dashboard-card">
                <Space direction="vertical" size="middle">
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
        </div>
    );
}
