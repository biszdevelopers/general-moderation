import {
    App as AntdApp,
    Button,
    Form,
    Input,
    InputNumber,
    Modal,
    Popconfirm,
    Select,
    Space,
    Table,
    Tag,
    Typography,
} from "antd";
import { PlusOutlined } from "@ant-design/icons";
import { TableProps } from "antd";
import { useEffect, useState } from "react";
import { ReactElement } from "react";
import { useAppContext } from "../contexts/AppContext";
import { PhraseEntry, PhrasePayload } from "../types";
import { LoadingSpinner } from "../components/LoadingSpinner";
import { LoginPrompt } from "../components/LoginPrompt";

const phraseCategories: string[] = [
    "profanity",
    "violence",
    "political",
    "hate_speech",
    "sexual",
    "other",
];

interface PhraseFormValues {
    phrase: string;
    language: string;
    category: string;
    severity: number;
}

export function Phrases(): ReactElement {
    const { phraseService, authenticated } = useAppContext();
    const { message } = AntdApp.useApp();
    const [phrases, setPhrases] = useState<PhraseEntry[]>([]);
    const [loading, setLoading] = useState<boolean>(true);
    const [modalOpen, setModalOpen] = useState<boolean>(false);
    const [editing, setEditing] = useState<PhraseEntry | null>(null);
    const [form] = Form.useForm<PhraseFormValues>();

    const loadPhrases = async (): Promise<void> => {
        try {
            setPhrases(await phraseService.list());
        } catch (error: unknown) {
            message.error(`Failed to load phrases: ${String(error)}`);
        }
    };

    useEffect(() => {
        if (!authenticated) {
            setLoading(false);
            return;
        }
        const load = async (): Promise<void> => {
            try {
                setPhrases(await phraseService.list());
            } catch (error: unknown) {
                message.error(`Failed to load phrases: ${String(error)}`);
            } finally {
                setLoading(false);
            }
        };
        void load();
    }, [phraseService, message, authenticated]);

    const openAddModal = (): void => {
        setEditing(null);
        form.resetFields();
        setModalOpen(true);
    };

    const openEditModal = (record: PhraseEntry): void => {
        setEditing(record);
        form.setFieldsValue({
            phrase: record.phrase,
            language: record.language,
            category: record.category,
            severity: record.severity,
        });
        setModalOpen(true);
    };

    const onSubmit = async (values: PhraseFormValues): Promise<void> => {
        const payload: PhrasePayload = {
            phrase: values.phrase,
            language: values.language,
            category: values.category,
            severity: values.severity,
        };
        try {
            if (editing !== null) {
                await phraseService.update(editing.id, payload);
                message.success("Phrase updated");
            } else {
                await phraseService.add(payload);
                message.success("Phrase added");
            }
            setModalOpen(false);
            await loadPhrases();
        } catch (error: unknown) {
            message.error(String(error));
        }
    };

    const onRemove = async (record: PhraseEntry): Promise<void> => {
        try {
            const result: { removed: boolean } = await phraseService.remove(record.id);
            if (result.removed) {
                message.success("Phrase removed");
            }
            await loadPhrases();
        } catch (error: unknown) {
            message.error(String(error));
        }
    };

    const columns: TableProps<PhraseEntry>["columns"] = [
        { title: "ID", dataIndex: "id", key: "id", width: 72 },
        {
            title: "Phrase",
            dataIndex: "phrase",
            key: "phrase",
            render: (value: string): ReactElement => (
                <Typography.Text code>{value}</Typography.Text>
            ),
        },
        { title: "Language", dataIndex: "language", key: "language" },
        {
            title: "Category",
            dataIndex: "category",
            key: "category",
            render: (value: string): ReactElement => <Tag color="blue">{value}</Tag>,
        },
        {
            title: "Severity",
            dataIndex: "severity",
            key: "severity",
            render: (value: number): ReactElement => (
                <Tag color={value >= 7 ? "red" : value >= 4 ? "orange" : "green"}>{value}</Tag>
            ),
        },
        { title: "Created At", dataIndex: "created_at", key: "created_at" },
        {
            title: "Actions",
            key: "actions",
            render: (_: unknown, record: PhraseEntry): ReactElement => (
                <Space>
                    <Button size="small" onClick={() => openEditModal(record)}>
                        Edit
                    </Button>
                    <Popconfirm title="Remove this phrase?" onConfirm={() => onRemove(record)}>
                        <Button size="small" danger>
                            Remove
                        </Button>
                    </Popconfirm>
                </Space>
            ),
        },
    ];

    if (!authenticated) {
        return <LoginPrompt />;
    }

    if (loading) {
        return <LoadingSpinner />;
    }

    return (
        <div className="page">
            <Typography.Title level={2} className="page__title">
                Critical Phrases
            </Typography.Title>
            <Typography.Paragraph className="page__subtitle">
                Manage the high-severity phrases that drive hard-block and suspicion-score floor
                policies.
            </Typography.Paragraph>
            <div className="wordbank-toolbar">
                <Typography.Text type="secondary">
                    {phrases.length} phrase{phrases.length === 1 ? "" : "s"} configured
                </Typography.Text>
                <Button type="primary" icon={<PlusOutlined />} onClick={openAddModal}>
                    Add Phrase
                </Button>
            </div>
            <Table<PhraseEntry>
                rowKey="id"
                columns={columns}
                dataSource={phrases}
                pagination={{ pageSize: 20 }}
                scroll={{ x: "max-content" }}
                locale={{ emptyText: "No critical phrases configured" }}
            />
            <Modal
                title={editing !== null ? "Edit Phrase" : "Add Phrase"}
                open={modalOpen}
                onCancel={() => setModalOpen(false)}
                onOk={() => void form.submit()}
                destroyOnHidden
            >
                <Form<PhraseFormValues>
                    form={form}
                    layout="vertical"
                    onFinish={(values) => void onSubmit(values)}
                >
                    <Form.Item
                        name="phrase"
                        label="Phrase"
                        rules={[{ required: true, message: "Phrase is required" }]}
                    >
                        <Input maxLength={200} />
                    </Form.Item>
                    <Form.Item name="language" label="Language" initialValue="any">
                        <Input maxLength={32} placeholder="any" />
                    </Form.Item>
                    <Form.Item
                        name="category"
                        label="Category"
                        initialValue="other"
                        rules={[{ required: true }]}
                    >
                        <Select
                            options={phraseCategories.map((category: string) => ({
                                value: category,
                                label: category,
                            }))}
                        />
                    </Form.Item>
                    <Form.Item
                        name="severity"
                        label="Severity"
                        initialValue={5}
                        rules={[{ required: true }]}
                    >
                        <InputNumber min={0} max={10} />
                    </Form.Item>
                </Form>
            </Modal>
        </div>
    );
}
