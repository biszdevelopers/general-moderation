import {
  App as AntdApp,
  Badge,
  Button,
  Card,
  Collapse,
  Descriptions,
  Drawer,
  Input,
  InputNumber,
  Select,
  Space,
  Switch,
  Table,
  Tag,
  Tooltip,
  Typography,
} from "antd";
import {
  HistoryOutlined,
  LockOutlined,
  PoweroffOutlined,
  ReloadOutlined,
  SaveOutlined,
  ThunderboltOutlined,
} from "@ant-design/icons";
import { useEffect, useMemo, useState } from "react";
import { ReactElement } from "react";
import { useAppContext } from "../contexts/AppContext";
import { ConfigAuditRecord, ConfigPreset, HealthReport, SettingRecord } from "../types";
import { LoadingSpinner } from "../components/LoadingSpinner";

const GROUP_ORDER: string[] = [
  "Models & Providers",
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

const LOG_LEVELS: string[] = ["DEBUG", "INFO", "WARNING", "ERROR"];

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
  const [search, setSearch] = useState<string>("");
  const [presets, setPresets] = useState<ConfigPreset[]>([]);
  const [historyOpen, setHistoryOpen] = useState<boolean>(false);
  const [history, setHistory] = useState<ConfigAuditRecord[]>([]);
  const [historyKey, setHistoryKey] = useState<string>("");

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
        if (!record.editable) {
          continue;
        }
        next[record.key] = record.secret ? "" : record.value;
      }
      setDraft(next);
    } catch (error: unknown) {
      message.error(`Failed to load settings: ${String(error)}`);
    }
  };

  const loadPresets = async (): Promise<void> => {
    try {
      const result: { presets: ConfigPreset[] } = await settingsService.getPresets();
      setPresets(result.presets);
    } catch {
      setPresets([]);
    }
  };

  const loadHistory = async (): Promise<void> => {
    try {
      const filter: string | undefined =
        historyKey.trim().length > 0 ? historyKey.trim().toUpperCase() : undefined;
      const result: { history: ConfigAuditRecord[] } = await settingsService.getHistory(
        filter,
        200,
      );
      setHistory(result.history);
    } catch (error: unknown) {
      message.error(`Failed to load history: ${String(error)}`);
    }
  };

  useEffect(() => {
    if (authenticated) {
      void refreshHealth();
      void loadSettings();
      void loadPresets();
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [authenticated]);

  const visibleRecords: SettingRecord[] = useMemo(() => {
    const needle: string = search.trim().toLowerCase();
    if (needle.length === 0) {
      return records;
    }
    return records.filter(
      (record) =>
        record.key.toLowerCase().includes(needle) ||
        record.description.toLowerCase().includes(needle),
    );
  }, [records, search]);

  const groups = useMemo(() => {
    const grouped: Record<string, SettingRecord[]> = {};
    for (const record of visibleRecords) {
      if (!record.editable && !record.restart_required) {
        continue;
      }
      const group: string = record.category ?? "Other";
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
  }, [visibleRecords]);

  const onSaveKey = (): void => {
    if (apiKey.trim().length === 0) {
      message.warning("Enter an API key");
      return;
    }
    login(apiKey.trim());
    message.success("API key saved");
    void refreshHealth();
    void loadSettings();
    void loadPresets();
  };

  const onClearKey = (): void => {
    logout();
    setApiKey("");
    setHealth(null);
    setRecords([]);
    setPresets([]);
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
      const changed: Record<string, string | number | boolean> = {};
      for (const record of records) {
        if (!record.editable || draft[record.key] === undefined) {
          continue;
        }
        if (record.secret) {
          const typed: string = String(draft[record.key]);
          if (typed.length > 0) {
            changed[record.key] = typed;
          }
          continue;
        }
        if (draft[record.key] !== record.value) {
          changed[record.key] = draft[record.key];
        }
      }
      if (Object.keys(changed).length === 0) {
        message.info("No changes to save");
        return;
      }
      const result: { status: string; updated: string[] } =
        await settingsService.updateSettings(changed);
      message.success(`Saved ${result.updated.length} setting(s)`);
      await loadSettings();
    } catch (error: unknown) {
      message.error(`Save failed: ${String(error)}`);
    } finally {
      setSaving(false);
    }
  };

  const onApplyPreset = (name: string): void => {
    modal.confirm({
      title: `Apply preset "${name}"?`,
      content: "Every setting in the preset is validated and applied in one batch.",
      okText: "Apply",
      onOk: async (): Promise<void> => {
        try {
          const result: { status: string; updated: string[] } =
            await settingsService.applyPreset(name);
          message.success(`Preset applied: ${result.updated.length} setting(s) changed`);
          await loadSettings();
        } catch (error: unknown) {
          message.error(`Preset failed: ${String(error)}`);
        }
      },
    });
  };

  const onRunTuning = async (): Promise<void> => {
    try {
      const report = await settingsService.runTuning();
      message.success(`Tuning complete (precision ${Math.round((report.precision ?? 0) * 100)}%)`);
      await loadSettings();
    } catch (error: unknown) {
      message.error(`Tuning failed: ${String(error)}`);
    }
  };

  const onShutdown = (): void => {
    modal.confirm({
      title: "Shut down the moderation service?",
      content: "This gracefully releases the model, word bank, and logger, then stops the process.",
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

  const openHistory = (): void => {
    setHistoryOpen(true);
    void loadHistory();
  };

  const setField = (key: string, value: string | number | boolean): void => {
    setDraft((current) => ({ ...current, [key]: value }));
  };

  const renderField = (record: SettingRecord): ReactElement => {
    const key: string = record.key;
    if (record.secret) {
      return (
        <Tooltip title="Stored encrypted; leave unchanged to keep the current value">
          <Input.Password
            placeholder="Set new value"
            value={typeof draft[key] === "string" ? String(draft[key]) : ""}
            onChange={(event) => setField(key, event.target.value)}
            style={{ width: 220 }}
            autoComplete="new-password"
          />
        </Tooltip>
      );
    }
    if (Array.isArray(record.choices)) {
      return (
        <Select
          value={String(draft[key])}
          onChange={(value) => setField(key, value)}
          style={{ width: 240 }}
          options={record.choices.map((choice) => ({
            value: choice,
            label: choice.length === 0 ? "(none)" : choice,
          }))}
        />
      );
    }
    if (record.type === "boolean") {
      return (
        <Switch checked={Boolean(draft[key])} onChange={(checked) => setField(key, checked)} />
      );
    }
    if (record.type === "integer" || record.type === "float") {
      return (
        <InputNumber
          value={Number(draft[key])}
          onChange={(value) => setField(key, value ?? 0)}
          step={record.type === "float" ? 0.01 : 1}
          min={record.min}
          max={record.max}
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
          options={LOG_LEVELS.map((level) => ({ value: level, label: level }))}
        />
      );
    }
    return (
      <Input
        value={String(draft[key])}
        onChange={(event) => setField(key, event.target.value)}
        style={{ width: 260 }}
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
      <Typography.Paragraph className="page__subtitle">
        Manage the admin API key, service health, and every runtime setting without a restart.
        Locked fields require a service restart.
      </Typography.Paragraph>
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
              <Badge status="success" text={health.status} />
            </Descriptions.Item>
            <Descriptions.Item label="Uptime">
              {Math.round(health.uptimeSeconds)} seconds
            </Descriptions.Item>
            <Descriptions.Item label="Total Words">{health.wordCount.totalWords}</Descriptions.Item>
            <Descriptions.Item label="Custom Words">
              {health.wordCount.customWords}
            </Descriptions.Item>
            <Descriptions.Item label="Base Words">{health.wordCount.baseWords}</Descriptions.Item>
            <Descriptions.Item label="Languages">{health.wordCount.languages}</Descriptions.Item>
            <Descriptions.Item label="Level 2 (llama.cpp)">
              {health.llamaAvailable ? "Available" : "Unavailable"}
            </Descriptions.Item>
            <Descriptions.Item label="Detectors">
              {health.detectors
                .map((detector) => `${detector.name}:${detector.available ? "ready" : "missing"}`)
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
            <Space wrap>
              <Input.Search
                allowClear
                placeholder="Search settings"
                value={search}
                onChange={(event) => setSearch(event.target.value)}
                style={{ width: 200 }}
              />
                            <Select
                                placeholder="Apply preset"
                                style={{ width: 170 }}
                                value={null}
                                onSelect={(name: unknown) => onApplyPreset(String(name))}
                                options={presets.map((preset) => ({
                                    value: preset.name,
                                    label: preset.name,
                                }))}
                            />
              <Button icon={<HistoryOutlined />} onClick={openHistory}>
                History
              </Button>
              <Button onClick={() => void onRunTuning()}>Run Auto-Tuning</Button>
              <Button
                type="primary"
                icon={<SaveOutlined />}
                loading={saving}
                onClick={() => void onSaveSettings()}
              >
                Save Changes
              </Button>
            </Space>
          }
        >
          <Collapse
            defaultActiveKey={groups.map((group) => group.name)}
            items={groups.map((group) => ({
              key: group.name,
              label: `${group.name} (${group.items.length})`,
              children: (
                <Space direction="vertical" style={{ width: "100%" }} size="middle">
                  {group.items.map((record) => (
                    <Space key={record.key} align="center" size="large" wrap>
                      <Typography.Text style={{ width: 300 }}>
                        {labelOf(record.key)}
                        {record.restart_required && !record.editable && (
                          <Tooltip title="Requires service restart">
                            <LockOutlined style={{ marginLeft: 8, color: "#faad14" }} />
                          </Tooltip>
                        )}
                      </Typography.Text>
                      {record.editable ? (
                        renderField(record)
                      ) : (
                        <Tooltip title="Requires service restart">
                          <Input value={String(record.value)} disabled style={{ width: 260 }} />
                        </Tooltip>
                      )}
                      <Typography.Text type="secondary" style={{ maxWidth: 420 }}>
                        {record.description}
                        {record.min !== undefined &&
                          record.max !== undefined &&
                          ` (${record.min} - ${record.max})`}
                      </Typography.Text>
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
          <Button icon={<ThunderboltOutlined />} onClick={() => void onRunTuning()}>
            Run Tuning Batch
          </Button>
        </Space>
      </Card>
      <Drawer
        title="Configuration Change History"
        width={720}
        open={historyOpen}
        onClose={() => setHistoryOpen(false)}
        extra={
          <Space>
            <Input
              allowClear
              placeholder="Filter by key"
              value={historyKey}
              onChange={(event) => setHistoryKey(event.target.value)}
              style={{ width: 180 }}
            />
            <Button icon={<ReloadOutlined />} onClick={() => void loadHistory()}>
              Refresh
            </Button>
          </Space>
        }
      >
        <Table<ConfigAuditRecord>
          size="small"
          rowKey={(record, index) => `${record.key}-${index}`}
          dataSource={history}
          pagination={{ pageSize: 20 }}
          columns={[
            { title: "Time", dataIndex: "created_at", width: 150 },
            { title: "Key", dataIndex: "key", width: 220 },
            { title: "Old", dataIndex: "old_value", ellipsis: true },
            { title: "New", dataIndex: "new_value", ellipsis: true },
            { title: "Source", dataIndex: "source", width: 130 },
          ]}
        />
      </Drawer>
    </div>
  );
}
