import { ReactElement, useEffect, useMemo, useState } from "react";
import {
    App as AntdApp,
    Button,
    Card,
    Collapse,
    InputNumber,
    Space,
    Switch,
    Typography,
} from "antd";
import { SaveOutlined, ReloadOutlined } from "@ant-design/icons";
import { useAppContext } from "../../contexts/AppContext";
import { SettingRecord } from "../../types";

interface ToggleEntry {
    key: string;
    label: string;
}

const DETECTOR_TOGGLES: ToggleEntry[] = [
    { key: "ENABLE_DETECTOR_BLOOM_FILTER", label: "Bloom Filter (fast negative)" },
    { key: "ENABLE_DETECTOR_ROLLING_HASH", label: "Rolling Hash (repeat spam)" },
    { key: "ENABLE_DETECTOR_AHO_CORASICK", label: "Aho-Corasick (exact match)" },
    { key: "ENABLE_DETECTOR_BK_TREE", label: "BK-Tree (fuzzy match)" },
    { key: "ENABLE_DETECTOR_DOUBLE_METAPHONE", label: "Double Metaphone (phonetic)" },
    { key: "ENABLE_DETECTOR_MULTI_LANGUAGE", label: "Multi-language packages" },
];

const STAGE_TOGGLES: ToggleEntry[] = [
    { key: "SAFE_WORD_ENABLED", label: "Stage 1 safe word fast path" },
    { key: "SEMANTIC_ENABLED", label: "Stage 2 semantic similarity" },
    { key: "USER_PROFILING_ENABLED", label: "Stage 2 user profiling" },
];

const WEIGHT_KEYS: string[] = [
    "WEIGHT_DETECTOR_BADWORDS",
    "WEIGHT_DETECTOR_PROFANITE",
    "WEIGHT_DETECTOR_GLIN",
    "WEIGHT_DETECTOR_AHO",
    "WEIGHT_DETECTOR_BKTREE",
    "WEIGHT_DETECTOR_METAPHONE",
    "WEIGHT_SEMANTIC_POLITICAL",
    "WEIGHT_SEMANTIC_VIOLENCE",
    "WEIGHT_SEMANTIC_SEXUAL",
    "WEIGHT_SEMANTIC_HATE",
    "WEIGHT_SEMANTIC_PII",
    "WEIGHT_SEMANTIC_ADS",
    "WEIGHT_USER",
];

const THRESHOLD_KEYS: string[] = [
    "SEMANTIC_SIMILARITY_THRESHOLD",
    "SEMANTIC_FORCE_LLM_THRESHOLD",
    "USER_RATIO_THRESHOLD",
    "AI_TARGET_PERCENTAGE",
    "USER_WINDOW_DAYS",
];

function labelOf(key: string): string {
    const spaced: string = key.replace(/_/g, " ").toLowerCase();
    return spaced.replace(/(^|\s)\S/g, (char) => char.toUpperCase());
}

export function ConfigPlayground(): ReactElement {
    const { testApiService } = useAppContext();
    const { message } = AntdApp.useApp();
    const [records, setRecords] = useState<SettingRecord[]>([]);
    const [draft, setDraft] = useState<Record<string, string | number | boolean>>({});
    const [saving, setSaving] = useState<boolean>(false);
    const [loading, setLoading] = useState<boolean>(false);

    const relevantKeys: string[] = useMemo(
        () => [
            ...DETECTOR_TOGGLES.map((entry) => entry.key),
            ...STAGE_TOGGLES.map((entry) => entry.key),
            ...WEIGHT_KEYS,
            ...THRESHOLD_KEYS,
        ],
        [],
    );

    const loadConfig = async (): Promise<void> => {
        setLoading(true);
        try {
            const result: { settings: SettingRecord[] } = await testApiService.getConfig();
            setRecords(result.settings);
            const next: Record<string, string | number | boolean> = {};
            for (const record of result.settings) {
                if (record.editable && relevantKeys.includes(record.key)) {
                    next[record.key] = record.value;
                }
            }
            setDraft(next);
        } catch (err: unknown) {
            message.error(`Failed to load configuration: ${String(err)}`);
        } finally {
            setLoading(false);
        }
    };

    useEffect(() => {
        void loadConfig();
    }, []);

    const setField = (key: string, value: string | number | boolean): void => {
        setDraft((current) => ({ ...current, [key]: value }));
    };

    const onSave = async (): Promise<void> => {
        setSaving(true);
        try {
            const result: { status: string; updated: string[] } =
                await testApiService.updateConfig(draft);
            message.success(`Applied ${result.updated.length} change(s)`);
            await loadConfig();
        } catch (err: unknown) {
            message.error(`Apply failed: ${String(err)}`);
        } finally {
            setSaving(false);
        }
    };

    const descriptionOf = (key: string): string => {
        const record: SettingRecord | undefined = records.find((entry) => entry.key === key);
        return record?.description ?? "";
    };

    const renderSwitch = (entry: ToggleEntry): ReactElement => (
        <Space key={entry.key} align="center" size="large" style={{ width: "100%" }}>
            <Typography.Text style={{ width: 320 }}>{entry.label}</Typography.Text>
            <Switch
                checked={Boolean(draft[entry.key])}
                onChange={(checked) => setField(entry.key, checked)}
            />
            <Typography.Text type="secondary">{descriptionOf(entry.key)}</Typography.Text>
        </Space>
    );

    const renderNumber = (key: string, min: number, max: number, step?: number): ReactElement => (
        <Space key={key} align="center" size="large" style={{ width: "100%" }}>
            <Typography.Text style={{ width: 320 }}>{labelOf(key)}</Typography.Text>
            <InputNumber
                value={Number(draft[key])}
                min={min}
                max={max}
                step={step ?? 1}
                onChange={(value) => setField(key, value ?? 0)}
                style={{ width: 160 }}
            />
            <Typography.Text type="secondary">{descriptionOf(key)}</Typography.Text>
        </Space>
    );

    return (
        <Card
            title="Configuration Playground"
            className="workbench-card"
            extra={
                <Space>
                    <Button
                        icon={<ReloadOutlined />}
                        loading={loading}
                        onClick={() => void loadConfig()}
                    >
                        Reload
                    </Button>
                    <Button
                        type="primary"
                        icon={<SaveOutlined />}
                        loading={saving}
                        onClick={() => void onSave()}
                    >
                        Apply Changes
                    </Button>
                </Space>
            }
        >
            <Typography.Paragraph type="secondary">
                Changes apply immediately to the interactive test. Detector toggles only affect the
                workbench pipeline; the production endpoint behavior is unchanged.
            </Typography.Paragraph>
            <Collapse
                defaultActiveKey={["detectors", "stage-toggles", "weights", "thresholds"]}
                items={[
                    {
                        key: "detectors",
                        label: `Detector Toggles (${DETECTOR_TOGGLES.length})`,
                        children: (
                            <Space direction="vertical" style={{ width: "100%" }} size="middle">
                                {DETECTOR_TOGGLES.map(renderSwitch)}
                            </Space>
                        ),
                    },
                    {
                        key: "stage-toggles",
                        label: "Pipeline Stage Toggles",
                        children: (
                            <Space direction="vertical" style={{ width: "100%" }} size="middle">
                                {STAGE_TOGGLES.map(renderSwitch)}
                            </Space>
                        ),
                    },
                    {
                        key: "weights",
                        label: `Suspicion Weights (${WEIGHT_KEYS.length})`,
                        children: (
                            <Space direction="vertical" style={{ width: "100%" }} size="middle">
                                {WEIGHT_KEYS.map((key) => renderNumber(key, 5, 50))}
                            </Space>
                        ),
                    },
                    {
                        key: "thresholds",
                        label: "Thresholds & Targets",
                        children: (
                            <Space direction="vertical" style={{ width: "100%" }} size="middle">
                                {renderNumber("SEMANTIC_SIMILARITY_THRESHOLD", 0, 1, 0.01)}
                                {renderNumber("SEMANTIC_FORCE_LLM_THRESHOLD", 0, 1, 0.01)}
                                {renderNumber("USER_RATIO_THRESHOLD", 0, 1, 0.01)}
                                {renderNumber("AI_TARGET_PERCENTAGE", 0, 100)}
                                {renderNumber("USER_WINDOW_DAYS", 7, 365)}
                            </Space>
                        ),
                    },
                ]}
            />
        </Card>
    );
}
