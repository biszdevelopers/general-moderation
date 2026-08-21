import {
  App as AntdApp,
  Badge,
  Button,
  Card,
  Descriptions,
  Form,
  Input,
  Modal,
  Select,
  Space,
  Table,
  Tag,
  Typography,
} from "antd";
import {
  CheckCircleOutlined,
  CloudDownloadOutlined,
  CloseCircleOutlined,
  FileAddOutlined,
  ReloadOutlined,
  UploadOutlined,
} from "@ant-design/icons";
import { useCallback, useEffect, useState } from "react";
import { ReactElement } from "react";
import { useAppContext } from "../contexts/AppContext";
import { ModelRecord, PromptVersionRecord, ProviderHealthReport, SettingRecord } from "../types";
import { LoadingSpinner } from "../components/LoadingSpinner";

const PROVIDER_LABELS: Record<string, string> = {
  local_llama_cpp: "Local llama.cpp (GGUF)",
  external_llama_cpp: "External llama.cpp server",
  ollama: "Ollama",
  openai_compatible: "OpenAI-compatible API",
  anthropic_compatible: "Anthropic-compatible API",
};

const PROVIDER_FIELDS: Record<string, string[]> = {
  local_llama_cpp: ["ACTIVE_GGUF_PATH"],
  external_llama_cpp: ["EXTERNAL_LLAMACPP_BASE_URL", "EXTERNAL_LLAMACPP_MODEL"],
  ollama: ["OLLAMA_BASE_URL", "OLLAMA_MODEL"],
  openai_compatible: ["OPENAI_BASE_URL", "OPENAI_MODEL", "OPENAI_API_KEY"],
  anthropic_compatible: ["ANTHROPIC_BASE_URL", "ANTHROPIC_MODEL", "ANTHROPIC_API_KEY"],
};

function formatBytes(size: number): string {
  if (size <= 0) {
    return "-";
  }
  const units: string[] = ["B", "KB", "MB", "GB"];
  let value: number = size;
  let unitIndex: number = 0;
  while (value >= 1024 && unitIndex < units.length - 1) {
    value /= 1024;
    unitIndex += 1;
  }
  return `${value.toFixed(value >= 10 || unitIndex === 0 ? 0 : 1)} ${units[unitIndex]}`;
}

export function ModelManagement(): ReactElement {
  const { authService, modelService, authenticated, login } = useAppContext();
  const { message, modal } = AntdApp.useApp();
  const [apiKey, setApiKey] = useState<string>(authService.getApiKey() ?? "");
  const [loading] = useState<boolean>(false);
  const [models, setModels] = useState<ModelRecord[]>([]);
  const [health, setHealth] = useState<ProviderHealthReport | null>(null);
  const [settingsRecords, setSettingsRecords] = useState<SettingRecord[]>([]);
  const [providerDraft, setProviderDraft] = useState<Record<string, string>>({});
  const [registerOpen, setRegisterOpen] = useState<boolean>(false);
  const [downloadOpen, setDownloadOpen] = useState<boolean>(false);
  const [uploadOpen, setUploadOpen] = useState<boolean>(false);
  const [promptOpen, setPromptOpen] = useState<boolean>(false);
  const [promptText, setPromptText] = useState<string>("");
  const [versions, setVersions] = useState<PromptVersionRecord[]>([]);
  const [uploadFile, setUploadFile] = useState<File | null>(null);
  const [registerForm] = Form.useForm<{ name: string; path: string }>();
  const [downloadForm] = Form.useForm<{ name: string; repo: string; filename: string }>();

  const loadAll = useCallback(async (): Promise<void> => {
    try {
      const result = await modelService.listModels();
      setModels(result.models);
      setHealth(result.providers);
      const records: SettingRecord[] = await modelService.getSettings();
      setSettingsRecords(records.filter((record) => record.editable));
      const nextDraft: Record<string, string> = {};
      for (const record of records) {
        if (record.editable && !record.secret) {
          nextDraft[record.key] = String(record.value);
        }
      }
      setProviderDraft(nextDraft);
    } catch (error: unknown) {
      message.error(`Failed to load models: ${String(error)}`);
    }
  }, [modelService, message]);

  useEffect(() => {
    if (authenticated) {
      void loadAll();
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [authenticated]);

  if (!authenticated) {
    return (
      <div className="page">
        <Typography.Title level={2} className="page__title">
          Model Management
        </Typography.Title>
        <Card title="Admin API Key" className="settings-card">
          <Space direction="vertical" style={{ width: "100%" }}>
            <Input.Password
              placeholder="Admin API key"
              value={apiKey}
              onChange={(event) => setApiKey(event.target.value)}
            />
            <Button
              type="primary"
              onClick={() => {
                if (apiKey.trim().length > 0) {
                  login(apiKey.trim());
                }
              }}
            >
              Unlock
            </Button>
          </Space>
        </Card>
      </div>
    );
  }

  if (loading && models.length === 0 && health === null) {
    return <LoadingSpinner />;
  }

  const activeProvider: string = String(providerDraft["LLM_PROVIDER"] ?? "local_llama_cpp");
  const providerKeys: string[] = PROVIDER_FIELDS[activeProvider] ?? PROVIDER_FIELDS.local_llama_cpp;

  const refreshProviderHealth = async (): Promise<void> => {
    try {
      setHealth(await modelService.getProviderHealth());
    } catch (error: unknown) {
      message.error(`Health probe failed: ${String(error)}`);
    }
  };

  const onSaveProvider = async (): Promise<void> => {
    try {
      const payload: Record<string, string> = { LLM_PROVIDER: activeProvider };
      for (const key of providerKeys) {
        const value: string = providerDraft[key] ?? "";
        if (key.endsWith("_KEY") && value.length === 0) {
          continue;
        }
        payload[key] = value;
      }
      await modelService.updateSettings(payload);
      message.success("Provider configuration saved");
      await loadAll();
    } catch (error: unknown) {
      message.error(`Save failed: ${String(error)}`);
    }
  };

  const onActivate = async (model: ModelRecord): Promise<void> => {
    try {
      await modelService.activateModel(model.id);
      message.success(`Activated "${model.name}"`);
      await loadAll();
    } catch (error: unknown) {
      message.error(`Activation failed: ${String(error)}`);
    }
  };

  const onDelete = (model: ModelRecord): void => {
    modal.confirm({
      title: `Remove registration "${model.name}"?`,
      content: "The file stays on disk; only the registry entry is removed.",
      okButtonProps: { danger: true },
      onOk: async (): Promise<void> => {
        try {
          await modelService.deleteModel(model.id);
          message.success("Registration removed");
          await loadAll();
        } catch (error: unknown) {
          message.error(String(error));
        }
      },
    });
  };

  const onRegisterSubmit = async (): Promise<void> => {
    const values = await registerForm.validateFields();
    try {
      await modelService.registerModel(values.name, values.path);
      message.success("Model registered");
      setRegisterOpen(false);
      registerForm.resetFields();
      await loadAll();
    } catch (error: unknown) {
      message.error(`Registration failed: ${String(error)}`);
    }
  };

  const onDownloadSubmit = async (): Promise<void> => {
    const values = await downloadForm.validateFields();
    try {
      await modelService.downloadModel(values.name, values.repo, values.filename);
      message.success("Download queued; refresh to watch progress");
      setDownloadOpen(false);
      downloadForm.resetFields();
      await loadAll();
    } catch (error: unknown) {
      message.error(`Download failed: ${String(error)}`);
    }
  };

  const onUploadSubmit = async (): Promise<void> => {
    if (uploadFile === null) {
      message.warning("Choose a .gguf file first");
      return;
    }
    try {
      await modelService.uploadModel(uploadFile.name.replace(/\.gguf$/i, ""), uploadFile);
      message.success("Upload complete");
      setUploadOpen(false);
      setUploadFile(null);
      await loadAll();
    } catch (error: unknown) {
      message.error(`Upload failed: ${String(error)}`);
    }
  };

  const openPromptEditor = async (): Promise<void> => {
    try {
      const current: { template: string } = await modelService.getPrompt();
      const history: { versions: PromptVersionRecord[] } = await modelService.listPromptVersions();
      setPromptText(current.template);
      setVersions(history.versions);
      setPromptOpen(true);
    } catch (error: unknown) {
      message.error(`Failed to load prompt: ${String(error)}`);
    }
  };

  const onSavePrompt = async (): Promise<void> => {
    try {
      await modelService.updatePrompt(promptText);
      message.success("System prompt saved and pushed to providers");
      const history: { versions: PromptVersionRecord[] } = await modelService.listPromptVersions();
      setVersions(history.versions);
    } catch (error: unknown) {
      message.error(`Prompt save failed: ${String(error)}`);
    }
  };

  const onActivateVersion = async (versionId: number): Promise<void> => {
    try {
      await modelService.activatePromptVersion(versionId);
      message.success("Version activated");
      const current: { template: string } = await modelService.getPrompt();
      setPromptText(current.template);
      const history: { versions: PromptVersionRecord[] } = await modelService.listPromptVersions();
      setVersions(history.versions);
    } catch (error: unknown) {
      message.error(String(error));
    }
  };

  return (
    <div className="page">
      <Typography.Title level={2} className="page__title">
        Model Management
      </Typography.Title>
      <Typography.Paragraph className="page__subtitle">
        Switch LLM providers, manage GGUF versions, monitor health, and edit the system prompt
        without a restart.
      </Typography.Paragraph>
      <Card
        title="Provider"
        className="settings-card"
        extra={
          <Space>
            <Button icon={<ReloadOutlined />} onClick={() => void refreshProviderHealth()}>
              Probe Health
            </Button>
            <Button type="primary" onClick={() => void onSaveProvider()}>
              Save Provider
            </Button>
          </Space>
        }
      >
        <Descriptions bordered size="small" column={1} style={{ marginBottom: 16 }}>
          <Descriptions.Item label="Active">
            {health?.active ? (
              <Badge
                status={health.active.available ? "success" : "error"}
                text={PROVIDER_LABELS[health.active.name ?? ""] ?? health.active.name ?? "none"}
              />
            ) : (
              <Tag color="orange">None</Tag>
            )}
          </Descriptions.Item>
          <Descriptions.Item label="Backup">
            {health?.backup ? (
              <Badge
                status={health.backup.available ? "success" : "default"}
                text={PROVIDER_LABELS[health.backup.name ?? ""] ?? "registered"}
              />
            ) : (
              <Tag>None</Tag>
            )}
          </Descriptions.Item>
          <Descriptions.Item label="Consecutive failures">
            {health?.consecutive_failures ?? 0}
          </Descriptions.Item>
        </Descriptions>
        <Space direction="vertical" style={{ width: "100%" }} size="middle">
          <Select
            style={{ width: 320 }}
            value={activeProvider}
            onChange={(value: string) =>
              setProviderDraft((current) => ({ ...current, LLM_PROVIDER: value }))
            }
            options={Object.entries(PROVIDER_LABELS).map(([value, label]) => ({
              value,
              label,
            }))}
          />
          {providerKeys.map((key) => {
            const record: SettingRecord | undefined = settingsRecords.find(
              (candidate) => candidate.key === key,
            );
            const isSecret: boolean = Boolean(record?.secret);
            return (
              <Space key={key} align="center" size="large">
                <Typography.Text style={{ width: 260 }}>{key}</Typography.Text>
                {isSecret ? (
                  <Input.Password
                    placeholder="Set new value"
                    value={providerDraft[key] ?? ""}
                    onChange={(event) =>
                      setProviderDraft((current) => ({
                        ...current,
                        [key]: event.target.value,
                      }))
                    }
                    style={{ width: 300 }}
                    autoComplete="new-password"
                  />
                ) : (
                  <Input
                    value={providerDraft[key] ?? ""}
                    onChange={(event) =>
                      setProviderDraft((current) => ({
                        ...current,
                        [key]: event.target.value,
                      }))
                    }
                    style={{ width: 300 }}
                  />
                )}
                <Typography.Text type="secondary">{record?.description}</Typography.Text>
              </Space>
            );
          })}
        </Space>
      </Card>
      <Card
        title="GGUF Models"
        className="settings-card"
        extra={
          <Space wrap>
            <Button icon={<ReloadOutlined />} onClick={() => void loadAll()}>
              Refresh
            </Button>
            <Button icon={<FileAddOutlined />} onClick={() => setRegisterOpen(true)}>
              Register Path
            </Button>
            <Button icon={<CloudDownloadOutlined />} onClick={() => setDownloadOpen(true)}>
              Download
            </Button>
            <Button icon={<UploadOutlined />} onClick={() => setUploadOpen(true)}>
              Upload
            </Button>
            <Button type="primary" onClick={() => void openPromptEditor()}>
              System Prompt
            </Button>
          </Space>
        }
      >
        <Table<ModelRecord>
          rowKey="id"
          dataSource={models}
          pagination={false}
          columns={[
            {
              title: "Name",
              dataIndex: "name",
              render: (name: string, record: ModelRecord) =>
                record.active ? (
                  <Space>
                    {name}
                    <Tag color="green">Active</Tag>
                  </Space>
                ) : (
                  name
                ),
            },
            { title: "Path / Repo", dataIndex: "path", ellipsis: true },
            {
              title: "Size",
              dataIndex: "size_bytes",
              width: 100,
              render: (size: number) => formatBytes(size),
            },
            {
              title: "Status",
              dataIndex: "status",
              width: 130,
              render: (status: ModelRecord["status"], record: ModelRecord) => (
                <Space>
                  {status === "ready" && <CheckCircleOutlined style={{ color: "#52c41a" }} />}
                  {status !== "ready" && (
                    <CloseCircleOutlined
                      style={{ color: status === "failed" ? "#ff4d4f" : "#faad14" }}
                    />
                  )}
                  {status}
                  {!record.exists && record.path !== null && <Tag color="red">missing</Tag>}
                </Space>
              ),
            },
            {
              title: "Actions",
              width: 200,
              render: (_: unknown, record: ModelRecord) => (
                <Space>
                  <Button
                    size="small"
                    type="link"
                    disabled={!record.exists || record.active}
                    onClick={() => void onActivate(record)}
                  >
                    Activate
                  </Button>
                  <Button size="small" type="link" danger onClick={() => onDelete(record)}>
                    Remove
                  </Button>
                </Space>
              ),
            },
          ]}
        />
      </Card>
      <Modal
        title="Register a GGUF already on the server"
        open={registerOpen}
        onOk={() => void onRegisterSubmit()}
        onCancel={() => setRegisterOpen(false)}
        okText="Register"
      >
        <Form form={registerForm} layout="vertical">
          <Form.Item
            name="name"
            label="Display name"
            rules={[{ required: true, message: "Enter a name" }]}
          >
            <Input placeholder="Qwen3.5-9B Q4_K_M" />
          </Form.Item>
          <Form.Item
            name="path"
            label="Absolute server path"
            rules={[{ required: true, message: "Enter the path" }]}
          >
            <Input placeholder="/opt/models/model.gguf" />
          </Form.Item>
        </Form>
      </Modal>
      <Modal
        title="Download a GGUF from Hugging Face"
        open={downloadOpen}
        onOk={() => void onDownloadSubmit()}
        onCancel={() => setDownloadOpen(false)}
        okText="Queue Download"
      >
        <Form form={downloadForm} layout="vertical">
          <Form.Item
            name="name"
            label="Display name"
            rules={[{ required: true, message: "Enter a name" }]}
          >
            <Input placeholder="Qwen3.5-9B Q5_K_M" />
          </Form.Item>
          <Form.Item
            name="repo"
            label="Repository id"
            rules={[{ required: true, message: "Enter the repository" }]}
          >
            <Input placeholder="bartowski/Qwen_Qwen3.5-9B-GGUF" />
          </Form.Item>
          <Form.Item
            name="filename"
            label="GGUF filename"
            rules={[{ required: true, message: "Enter the filename" }]}
          >
            <Input placeholder="Qwen_Qwen3.5-9B-Q5_K_M.gguf" />
          </Form.Item>
        </Form>
      </Modal>
      <Modal
        title="Upload a GGUF file"
        open={uploadOpen}
        onOk={() => void onUploadSubmit()}
        onCancel={() => {
          setUploadOpen(false);
          setUploadFile(null);
        }}
        okText="Upload"
      >
        <input
          type="file"
          accept=".gguf"
          onChange={(event) => setUploadFile(event.target.files?.[0] ?? null)}
        />
        <Typography.Text type="secondary">
          Large files may take several minutes to upload.
        </Typography.Text>
      </Modal>
      <Modal
        title="Editable System Prompt"
        open={promptOpen}
        onCancel={() => setPromptOpen(false)}
        footer={[
          <Button key="close" onClick={() => setPromptOpen(false)}>
            Close
          </Button>,
          <Button key="save" type="primary" onClick={() => void onSavePrompt()}>
            Save New Version
          </Button>,
        ]}
        width={720}
      >
        <Input.TextArea
          rows={6}
          value={promptText}
          onChange={(event) => setPromptText(event.target.value)}
        />
        <Typography.Paragraph type="secondary" style={{ marginTop: 8 }}>
          Saving creates a new version and activates it immediately.
        </Typography.Paragraph>
        <Table<PromptVersionRecord>
          size="small"
          rowKey="id"
          dataSource={versions}
          pagination={false}
          columns={[
            { title: "ID", dataIndex: "id", width: 60 },
            { title: "Preview", dataIndex: "preview", ellipsis: true },
            {
              title: "Active",
              dataIndex: "active",
              width: 90,
              render: (active: boolean) => (active ? <Tag color="green">Active</Tag> : ""),
            },
            { title: "Created", dataIndex: "created_at", width: 160 },
            {
              title: "",
              width: 110,
              render: (_: unknown, record: PromptVersionRecord) =>
                !record.active && (
                  <Button
                    size="small"
                    type="link"
                    onClick={() => void onActivateVersion(record.id)}
                  >
                    Activate
                  </Button>
                ),
            },
          ]}
        />
      </Modal>
    </div>
  );
}
