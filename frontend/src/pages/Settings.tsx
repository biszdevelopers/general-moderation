import {
    App as AntdApp,
    Button,
    Card,
    Collapse,
    Descriptions,
    Input,
    InputNumber,
    Select,
    Space,
    Switch,
    Tag,
    Typography,
} from "antd";
import { LockOutlined, PoweroffOutlined, ReloadOutlined, SaveOutlined } from "@ant-design/icons";
import { useEffect, useMemo, useState } from "react";
import { ReactElement } from "react";
import { useAppContext } from "../contexts/AppContext";
import { HealthReport, SettingRecord } from "../types";
import { LoadingSpinner } from "../components/LoadingSpinner";

const GROUP_ORDER: string[] = [
    "Model",
    "Stage 1 Fast Path",
    "Detectors",
    "Detector Weights",
    "Semantic Similarity",
    "Semantic Weights",
    "User Profiling",
    "Suspicion Scoring",
    "LLM",
    "Feedback & Auto-Tuning",
    "Performance",
    "Security",
    "Logging",
    "Export",
];

function groupName(key: string): string {
    if (key.startsWith("MODEL_")) {
        return "Model";
    }
    if (key.startsWith("SAFE_WORD_")) {
        return "Stage 1 Fast Path";
    }
    if (key.startsWith("ENABLE_")) {
        return "Detectors";
    }
    if (key.startsWith("WEIGHT_DETECTOR_")) {
        return "Detector Weights";
    }
    if (key.startsWith("WEIGHT_SEMANTIC_")) {
        return "Semantic Weights";
    }
    if (key.startsWith("SEMANTIC_")) {
        return "Semantic Similarity";
    }
    if (key.startsWith("USER_")) {
        return "User Profiling";
    }
    if (key.startsWith("WEIGHT_USER") || key.startsWith("SCORE_WEIGHTS")) {
        return "Suspicion Scoring";
    }
    if (key.startsWith("AI_") || key.startsWith("FORCE_LLM_") || key.startsWith("LLM_")) {
        return "LLM";
    }
    if (key.startsWith("AUTO_TUNING_") || key.startsWith("WEIGHT_DECAY")) {
        return "Feedback & Auto-Tuning";
    }
    if (
        key.startsWith("CACHE_") ||
        key.startsWith("DETECTOR_THREAD") ||
        key.startsWith("REQUEST_") ||
        key.startsWith("MAX_BATCH")
    ) {
        return "Performance";
    }
    if (key.startsWith("RATE_LIMIT_") || key.startsWith("ALLOWED_ORIGINS")) {
        return "Security";
    }
    if (key.startsWith("LOG_")) {
        return "Logging";
    }
    if (key.startsWith("EXPORT_")) {
        return "Export";
    }
    return "Other";
}

function labelOf(key: string): string {
    const spaced: string = key.replace(/_/g, " ").toLowerCase();
    return spaced.replace(/(^|\s)\S/g, (char) => char.toUpperCase());
}

export function Settings(): ReactElement {
    const { authService, settingsService, authenticated, login, logout } = useAppContext();
    const { message, modal } = AntdApp.useApp();
    const [apiKey, setApiKey] = useState<string>(authService.getApiKey() ?? "");
    const [health, setHealth] = useState<HealthReport | null>(null);
    const [records, setRecords] = useState<SettingRecord[]>([]);
    const [draft, setDraft] = useState<Record<string, string | number | boolean>>({});
    const [loading, setLoading] = useState<boolean>(false);
    const [saving, setSaving] = useState<boolean>(false);

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

    const loadSettings = async (): Promise<void> => {
        try {
            const result: { settings: SettingRecord[] } = await settingsService.getSettings();
            setRecords(result.settings);
            const next: Record<string, string | number | boolean> = {};
            for (const record of result.settings) {
                if (record.editable) {
                    next[record.key] = record.value;
                }
            }
            setDraft(next);
        } catch (error: unknown) {
            message.error(`Failed to load settings: ${String(error)}`);
        }
    };

    useEffect(() => {
        if (authenticated) {
            void refreshHealth();
            void loadSettings();
        }
    }, [authenticated]);

    const groups = useMemo(() => {
        const grouped: Record<string, SettingRecord[]> = {};
        for (const record of records) {
            if (!record.editable) {
                continue;
            }
            const group: string = groupName(record.key);
            (grouped[group] ??= []).push(record);
        }
        const ordered: { name: string; items: SettingRecord[] }[] = [];
        for (const name of GROUP_ORDER) {
            if (grouped[name] !== undefined) {
                ordered.push({ name, items: grouped[name] });
            }
        }
        for (const [name, items] of Object.entries(grouped)) {
            if (!GROUP_ORDER.includes(name)) {
                ordered.push({ name, items });
            }
        }
        return ordered;
    }, [records]);

    const onSaveKey = (): void => {
        if (apiKey.trim().length === 0) {
            message.warning("Enter an API key");
            return;
        }
        login(apiKey.trim());
        message.success("API key saved");
        void refreshHealth();
        void loadSettings();
    };

    const onClearKey = (): void => {
        logout();
        setApiKey("");
        setHealth(null);
        setRecords([]);
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

    const onSaveSettings = async (): Promise<void> => {
        setSaving(true);
        try {
            const result: { status: string; updated: string[] } =
                await settingsService.updateSettings(draft);
            message.success(`Saved ${result.updated.length} setting(s)`);
            await loadSettings();
        } catch (error: unknown) {
            message.error(`Save failed: ${String(error)}`);
        } finally {
            setSaving(false);
        }
    };

    const onRunTuning = async (): Promise<void> => {
        try {
            const report = await settingsService.runTuning();
            message.success(
                `Tuning complete (precision ${Math.round((report.precision ?? 0) * 100)}%)`,
            );
            await loadSettings();
        } catch (error: unknown) {
            message.error(`Tuning failed: ${String(error)}`);
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

    const setField = (key: string, value: string | number | boolean): void => {
        setDraft((current) => ({ ...current, [key]: value }));
    };

    const renderField = (record: SettingRecord): ReactElement => {
        const key: string = record.key;
        if (record.type === "boolean") {
            return (
                <Switch
                    checked={Boolean(draft[key])}
                    onChange={(checked) => setField(key, checked)}
                />
            );
        }
        if (record.type === "integer") {
            return (
                <InputNumber
                    value={Number(draft[key])}
                    onChange={(value) => setField(key, value ?? 0)}
                    style={{ width: 160 }}
                />
            );
        }
        if (record.type === "float") {
            return (
                <InputNumber
                    value={Number(draft[key])}
                    onChange={(value) => setField(key, value ?? 0)}
                    step={0.01}
                    style={{ width: 160 }}
                />
            );
        }
        if (key === "LOG_LEVEL") {
            return (
                <Select
                    value={String(draft[key])}
                    onChange={(value) => setField(key, value)}
                    style={{ width: 160 }}
                    options={["DEBUG", "INFO", "WARNING", "ERROR"].map((level) => ({
                        value: level,
                        label: level,
                    }))}
                />
            );
        }
        if (key === "ALLOWED_ORIGINS") {
            return (
                <Input
                    value={String(draft[key])}
                    onChange={(event) => setField(key, event.target.value)}
                    style={{ width: 320 }}
                />
            );
        }
        return (
            <Input
                value={String(draft[key])}
                onChange={(event) => setField(key, event.target.value)}
                style={{ width: 200 }}
            />
        );
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
                        {authenticated && <Tag color="green">Authenticated</Tag>}
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
            {records.length > 0 && (
                <Card
                    title="Runtime Settings"
                    className="settings-card"
                    extra={
                        <Space>
                            <Button onClick={() => void onRunTuning()}>Run Auto-Tuning</Button>
                            <Button
                                type="primary"
                                icon={<SaveOutlined />}
                                loading={saving}
                                onClick={() => void onSaveSettings()}
                            >
                                Save All
                            </Button>
                        </Space>
                    }
                >
                    <Collapse
                        defaultActiveKey={groups.map((group) => group.name)}
                        items={groups.map((group) => ({
                            key: group.name,
                            label: group.name,
                            children: (
                                <Space direction="vertical" style={{ width: "100%" }} size="middle">
                                    {group.items.map((record) => (
                                        <Space key={record.key} align="center" size="large">
                                            <Typography.Text style={{ width: 300 }}>
                                                {labelOf(record.key)}
                                            </Typography.Text>
                                            {renderField(record)}
                                            {record.description.length > 0 && (
                                                <Typography.Text type="secondary">
                                                    {record.description}
                                                </Typography.Text>
                                            )}
                                        </Space>
                                    ))}
                                </Space>
                            ),
                        }))}
                    />
                </Card>
            )}
            <Card title="Service Control" className="settings-card">
                <Space>
                    <Button icon={<ReloadOutlined />} onClick={() => void onReload()}>
                        Reload Word Bank
                    </Button>
                    <Button danger icon={<PoweroffOutlined />} onClick={onShutdown}>
                        Graceful Shutdown
                    </Button>
                </Space>
            </Card>
        </div>
    );
}
