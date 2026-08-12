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
import { PlusOutlined, DownloadOutlined, UploadOutlined } from "@ant-design/icons";
import { TableProps } from "antd";
import { useEffect, useState } from "react";
import { ReactElement } from "react";
import { useAppContext } from "../contexts/AppContext";
import { WordEntry, WordPayload } from "../types";
import { LoadingSpinner } from "../components/LoadingSpinner";
import { LoginPrompt } from "../components/LoginPrompt";

const defaultCategories: string[] = [
    "profanity",
    "violence",
    "political",
    "hate_speech",
    "sexual",
    "other",
];

interface WordFormValues {
    word: string;
    language: string;
    category: string;
    severity: number;
}

export function WordBank(): ReactElement {
    const { wordBankService, authenticated } = useAppContext();
    const { message } = AntdApp.useApp();
    const [words, setWords] = useState<WordEntry[]>([]);
    const [categories, setCategories] = useState<string[]>(defaultCategories);
    const [languages, setLanguages] = useState<string[]>([]);
    const [loading, setLoading] = useState<boolean>(true);
    const [search, setSearch] = useState<string>("");
    const [categoryFilter, setCategoryFilter] = useState<string>("all");
    const [modalOpen, setModalOpen] = useState<boolean>(false);
    const [importOpen, setImportOpen] = useState<boolean>(false);
    const [editing, setEditing] = useState<WordEntry | null>(null);
    const [form] = Form.useForm<WordFormValues>();
    const [importForm] = Form.useForm<{ payload: string }>();

    const loadWords = async (): Promise<void> => {
        try {
            setWords(await wordBankService.listWords(search));
        } catch (error: unknown) {
            message.error(`Failed to load words: ${String(error)}`);
        }
    };

    useEffect(() => {
        if (!authenticated) {
            setLoading(false);
            return;
        }
        const loadAll = async (): Promise<void> => {
            try {
                const [wordList, categoryList, languageList] = await Promise.all([
                    wordBankService.listWords(),
                    wordBankService.getCategories(),
                    wordBankService.getLanguages(),
                ]);
                setWords(wordList);
                if (categoryList.length > 0) {
                    setCategories(categoryList);
                }
                setLanguages(languageList);
            } catch (error: unknown) {
                message.error(`Failed to load word bank: ${String(error)}`);
            } finally {
                setLoading(false);
            }
        };
        void loadAll();
    }, [wordBankService, message, authenticated]);

    const openAddModal = (): void => {
        setEditing(null);
        form.resetFields();
        setModalOpen(true);
    };

    const openEditModal = (record: WordEntry): void => {
        setEditing(record);
        form.setFieldsValue({
            word: record.word,
            language: record.language,
            category: record.category,
            severity: record.severity,
        });
        setModalOpen(true);
    };

    const onSubmit = async (values: WordFormValues): Promise<void> => {
        const payload: WordPayload = {
            word: values.word,
            language: values.language,
            category: values.category,
            severity: values.severity,
        };
        try {
            if (editing !== null) {
                await wordBankService.updateWord(editing.id, payload);
                message.success("Word updated");
            } else {
                await wordBankService.addWord(payload);
                message.success("Word added");
            }
            setModalOpen(false);
            await loadWords();
        } catch (error: unknown) {
            message.error(String(error));
        }
    };

    const onRemove = async (record: WordEntry): Promise<void> => {
        try {
            const result: { removed: boolean } = await wordBankService.removeWord(record.id);
            if (result.removed) {
                message.success("Word removed");
            }
            await loadWords();
        } catch (error: unknown) {
            message.error(String(error));
        }
    };

    const onExport = async (): Promise<void> => {
        try {
            const exported: WordEntry[] = await wordBankService.exportWords();
            const blob: Blob = new Blob([JSON.stringify(exported, null, 4)], {
                type: "application/json",
            });
            const url: string = URL.createObjectURL(blob);
            const anchor: HTMLAnchorElement = document.createElement("a");
            anchor.href = url;
            anchor.download = "word-bank-export.json";
            anchor.click();
            URL.revokeObjectURL(url);
            message.success(`Exported ${exported.length} words`);
        } catch (error: unknown) {
            message.error(String(error));
        }
    };

    const onImport = async (values: { payload: string }): Promise<void> => {
        try {
            const parsed: unknown = JSON.parse(values.payload);
            if (!Array.isArray(parsed)) {
                throw new Error("Payload must be a JSON array");
            }
            const items: WordPayload[] = parsed.map((item: unknown): WordPayload => {
                const entry: WordPayload = item as WordPayload;
                return {
                    word: String(entry.word),
                    language: String(entry.language ?? "any"),
                    category: String(entry.category ?? "other"),
                    severity: Number(entry.severity ?? 1),
                };
            });
            const result: { imported: number } = await wordBankService.importWords(items);
            message.success(`Imported ${result.imported} words`);
            setImportOpen(false);
            importForm.resetFields();
            await loadWords();
        } catch (error: unknown) {
            message.error(`Import failed: ${String(error)}`);
        }
    };

    const filteredWords: WordEntry[] =
        categoryFilter === "all"
            ? words
            : words.filter((word: WordEntry): boolean => word.category === categoryFilter);

    const columns: TableProps<WordEntry>["columns"] = [
        { title: "Word", dataIndex: "word", key: "word" },
        { title: "Language", dataIndex: "language", key: "language" },
        { title: "Category", dataIndex: "category", key: "category" },
        {
            title: "Severity",
            dataIndex: "severity",
            key: "severity",
            render: (value: number): ReactElement => (
                <Tag color={value >= 5 ? "red" : "orange"}>{value}</Tag>
            ),
        },
        { title: "Created At", dataIndex: "createdAt", key: "createdAt" },
        {
            title: "Actions",
            key: "actions",
            render: (_: unknown, record: WordEntry): ReactElement => (
                <Space>
                    <Button size="small" onClick={() => openEditModal(record)}>
                        Edit
                    </Button>
                    <Popconfirm title="Remove this word?" onConfirm={() => onRemove(record)}>
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
                Word Bank
            </Typography.Title>
            <Typography.Paragraph className="page__subtitle">
                Manage the custom words that feed the detection pipeline.
            </Typography.Paragraph>
            <div className="wordbank-toolbar">
                <Input.Search
                    placeholder="Search words"
                    allowClear
                    onSearch={(value: string) => {
                        setSearch(value);
                        void loadWords();
                    }}
                    className="wordbank-toolbar__search"
                />
                <Space>
                    <Select
                        value={categoryFilter}
                        onChange={setCategoryFilter}
                        className="wordbank-toolbar__category"
                        options={[
                            { value: "all", label: "All Categories" },
                            ...categories.map((category: string) => ({
                                value: category,
                                label: category,
                            })),
                        ]}
                    />
                    <Button icon={<DownloadOutlined />} onClick={() => void onExport()}>
                        Export
                    </Button>
                    <Button icon={<UploadOutlined />} onClick={() => setImportOpen(true)}>
                        Import
                    </Button>
                    <Button type="primary" icon={<PlusOutlined />} onClick={openAddModal}>
                        Add Word
                    </Button>
                </Space>
            </div>
            <Table<WordEntry>
                rowKey="id"
                columns={columns}
                dataSource={filteredWords}
                pagination={{ pageSize: 20 }}
                locale={{ emptyText: "No words match your filters" }}
            />
            <Modal
                title={editing !== null ? "Edit Word" : "Add Word"}
                open={modalOpen}
                onCancel={() => setModalOpen(false)}
                onOk={() => void form.submit()}
                destroyOnHidden
            >
                <Form<WordFormValues>
                    form={form}
                    layout="vertical"
                    onFinish={(values) => void onSubmit(values)}
                >
                    <Form.Item
                        name="word"
                        label="Word"
                        rules={[{ required: true, message: "Word is required" }]}
                    >
                        <Input maxLength={200} />
                    </Form.Item>
                    <Form.Item name="language" label="Language" initialValue="any">
                        <Select
                            showSearch
                            options={languages.map((language: string) => ({
                                value: language,
                                label: language,
                            }))}
                            placeholder="any"
                        />
                    </Form.Item>
                    <Form.Item
                        name="category"
                        label="Category"
                        initialValue="other"
                        rules={[{ required: true }]}
                    >
                        <Select
                            options={categories.map((category: string) => ({
                                value: category,
                                label: category,
                            }))}
                        />
                    </Form.Item>
                    <Form.Item
                        name="severity"
                        label="Severity"
                        initialValue={1}
                        rules={[{ required: true }]}
                    >
                        <InputNumber min={0} max={10} />
                    </Form.Item>
                </Form>
            </Modal>
            <Modal
                title="Import Words"
                open={importOpen}
                onCancel={() => setImportOpen(false)}
                onOk={() => void importForm.submit()}
                destroyOnHidden
            >
                <Form<{ payload: string }>
                    form={importForm}
                    layout="vertical"
                    onFinish={(values) => void onImport(values)}
                >
                    <Form.Item
                        name="payload"
                        label="JSON array"
                        rules={[{ required: true, message: "Payload is required" }]}
                    >
                        <Input.TextArea
                            rows={8}
                            placeholder='[{"word":"badword","language":"en","category":"profanity","severity":5}]'
                        />
                    </Form.Item>
                </Form>
            </Modal>
        </div>
    );
}
