import {
    App as AntdApp,
    Button,
    Card,
    Descriptions,
    Input,
    Modal,
    Space,
    Tag,
    Typography,
} from "antd";
import { LockOutlined, PoweroffOutlined, ReloadOutlined } from "@ant-design/icons";
import { useEffect, useState } from "react";
import { ReactElement } from "react";
import { useAppContext } from "../contexts/AppContext";
import { HealthReport } from "../types";
import { LoadingSpinner } from "../components/LoadingSpinner";

export function Settings(): ReactElement {
    const { authService, settingsService, authenticated, login, logout } = useAppContext();
    const { message, modal } = AntdApp.useApp();
    const [apiKey, setApiKey] = useState<string>(authService.getApiKey() ?? "");
    const [health, setHealth] = useState<HealthReport | null>(null);
    const [loading, setLoading] = useState<boolean>(false);

    const refreshHealth = async (): Promise<void> => {
        setLoading(true);
        try {
            setHealth(await settingsService.getHealth());
        } catch (error: unknown) {
            message.error(`Health check failed: ${String(error)}`);
        } finally {
            setLoading(false);
        }
    };

    useEffect(() => {
        if (authenticated) {
            void refreshHealth();
        }
    }, [authenticated]);

    const onSaveKey = (): void => {
        if (apiKey.trim().length === 0) {
            message.warning("Enter an API key");
            return;
        }
        login(apiKey.trim());
        message.success("API key saved");
        void refreshHealth();
    };

    const onClearKey = (): void => {
        logout();
        setApiKey("");
        setHealth(null);
        message.success("API key cleared");
    };

    const onReload = async (): Promise<void> => {
        try {
            const result: { status: string } = await settingsService.reload();
            message.success(`Word bank reloaded: ${result.status}`);
            await refreshHealth();
        } catch (error: unknown) {
            message.error(String(error));
        }
    };

    const onShutdown = (): void => {
        modal.confirm({
            title: "Shut down the moderation service?",
            content:
                "This gracefully releases the model, word bank, and logger, then stops the process.",
            okText: "Shut Down",
            okButtonProps: { danger: true },
            onOk: async (): Promise<void> => {
                try {
                    await settingsService.shutdown();
                    message.success("Shutdown request accepted");
                } catch (error: unknown) {
                    message.error(String(error));
                }
            },
        });
    };

    if (loading && health === null) {
        return <LoadingSpinner />;
    }

    return (
        <div className="page">
            <Typography.Title level={2} className="page__title">
                Settings
            </Typography.Title>
            <Card title="Admin API Key" className="settings-card">
                <Space direction="vertical" style={{ width: "100%" }} size="middle">
                    <Input.Password
                        prefix={<LockOutlined />}
                        placeholder="Admin API key"
                        value={apiKey}
                        onChange={(event) => setApiKey(event.target.value)}
                    />
                    <Space>
                        <Button type="primary" onClick={onSaveKey}>
                            Save Key
                        </Button>
                        <Button onClick={onClearKey}>Clear Key</Button>
                        {authenticated && (
                            <Tag color="green">Authenticated</Tag>
                        )}
                    </Space>
                </Space>
            </Card>
            <Card title="Service Health" className="settings-card">
                {health === null ? (
                    <Typography.Text type="secondary">
                        No health data. Save an API key to load the report.
                    </Typography.Text>
                ) : (
                    <Descriptions bordered size="small" column={1}>
                        <Descriptions.Item label="Status">
                            <Tag color="green">{health.status}</Tag>
                        </Descriptions.Item>
                        <Descriptions.Item label="Uptime">
                            {Math.round(health.uptimeSeconds)} seconds
                        </Descriptions.Item>
                        <Descriptions.Item label="Total Words">
                            {health.wordCount.totalWords}
                        </Descriptions.Item>
                        <Descriptions.Item label="Custom Words">
                            {health.wordCount.customWords}
                        </Descriptions.Item>
                        <Descriptions.Item label="Base Words">
                            {health.wordCount.baseWords}
                        </Descriptions.Item>
                        <Descriptions.Item label="Languages">
                            {health.wordCount.languages}
                        </Descriptions.Item>
                        <Descriptions.Item label="Level 2 (llama.cpp)">
                            {health.llamaAvailable ? "Available" : "Unavailable"}
                        </Descriptions.Item>
                        <Descriptions.Item label="Detectors">
                            {health.detectors
                                .map(
                                    (detector) =>
                                        `${detector.name}:${detector.available ? "ready" : "missing"}`,
                                )
                                .join(", ")}
                        </Descriptions.Item>
                    </Descriptions>
                )}
            </Card>
            <Card title="Service Control" className="settings-card">
                <Space>
                    <Button icon={<ReloadOutlined />} onClick={() => void onReload()}>
                        Reload Word Bank
                    </Button>
                    <Button
                        danger
                        icon={<PoweroffOutlined />}
                        onClick={onShutdown}
                    >
                        Graceful Shutdown
                    </Button>
                </Space>
            </Card>
        </div>
    );
}
