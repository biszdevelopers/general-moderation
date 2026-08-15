import {
    App as AntdApp,
    Button,
    Card,
    Descriptions,
    Form,
    Input,
    Popconfirm,
    Select,
    Table,
    Tag,
    Typography,
} from "antd";
import { DeleteOutlined, PlusOutlined, ReloadOutlined } from "@ant-design/icons";
import { TableProps } from "antd";
import { useEffect, useState } from "react";
import { ReactElement } from "react";
import { useAppContext } from "../contexts/AppContext";
import { SemanticStatus } from "../types";
import { LoadingSpinner } from "../components/LoadingSpinner";
import { LoginPrompt } from "../components/LoginPrompt";

const fallbackCategories: string[] = [
    "political",
    "violence",
    "sexual",
    "hate",
    "pii",
    "ads",
    "other",
];

interface CategoryRow {
    name: string;
    count: number;
}

export function Semantic(): ReactElement {
    const { semanticIndexService, authenticated } = useAppContext();
    const { message } = AntdApp.useApp();
    const [status, setStatus] = useState<SemanticStatus | null>(null);
    const [categories, setCategories] = useState<string[]>(fallbackCategories);
    const [loading, setLoading] = useState<boolean>(true);
    const [addForm] = Form.useForm<{ category: string; text: string }>();
    const [deleteForm] = Form.useForm<{ category: string; text: string }>();

    const loadStatus = async (): Promise<void> => {
        try {
            setStatus(await semanticIndexService.getStatus());
        } catch (error: unknown) {
            message.error(`Failed to load semantic index: ${String(error)}`);
        }
    };

    useEffect(() => {
        if (!authenticated) {
            setLoading(false);
            return;
        }
        const load = async (): Promise<void> => {
            try {
                const [current, knownCategories] = await Promise.all([
                    semanticIndexService.getStatus(),
                    semanticIndexService.getCategories(),
                ]);
                setStatus(current);
                if (knownCategories.length > 0) {
                    setCategories(knownCategories);
                }
            } catch (error: unknown) {
                message.error(`Failed to load semantic index: ${String(error)}`);
            } finally {
                setLoading(false);
            }
        };
        void load();
    }, [semanticIndexService, message, authenticated]);

    const onSubmitAdd = async (values: { category: string; text: string }): Promise<void> => {
        try {
            await semanticIndexService.add(values.category, values.text.trim());
            message.success("Example added");
            addForm.resetFields();
            await loadStatus();
        } catch (error: unknown) {
            message.error(String(error));
        }
    };

    const onSubmitDelete = async (values: { category: string; text: string }): Promise<void> => {
        try {
            await semanticIndexService.delete(values.category, values.text.trim());
            message.success("Example deleted");
            deleteForm.resetFields();
            await loadStatus();
        } catch (error: unknown) {
            message.error(String(error));
        }
    };

    const categoryOptions = categories.map((category: string) => ({
        value: category,
        label: category,
    }));

    const rows: CategoryRow[] =
        status !== null
            ? categories.map((category: string) => ({
                  name: category,
                  count: status.categories[category] ?? 0,
              }))
            : [];

    const columns: TableProps<CategoryRow>["columns"] = [
        {
            title: "Category",
            dataIndex: "name",
            key: "name",
            render: (value: string): ReactElement => <Tag color="blue">{value}</Tag>,
        },
        {
            title: "Examples",
            dataIndex: "count",
            key: "count",
            render: (value: number): ReactElement => (
                <Typography.Text strong>{value}</Typography.Text>
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
                Semantic Index
            </Typography.Title>
            <Typography.Paragraph className="page__subtitle">
                Inspect the semantic similarity index and manage the sensitive example texts per
                category.
            </Typography.Paragraph>
            <Card
                title="Index Status"
                className="settings-card"
                extra={
                    <Button icon={<ReloadOutlined />} onClick={() => void loadStatus()}>
                        Refresh
                    </Button>
                }
            >
                {status === null ? (
                    <Typography.Text type="secondary">No status available.</Typography.Text>
                ) : (
                    <Descriptions bordered size="small" column={1}>
                        <Descriptions.Item label="Available">
                            <Tag color={status.available ? "green" : "red"}>
                                {status.available ? "Available" : "Unavailable"}
                            </Tag>
                        </Descriptions.Item>
                        <Descriptions.Item label="Ready">
                            <Tag color={status.ready ? "green" : "orange"}>
                                {status.ready ? "Ready" : "Not loaded"}
                            </Tag>
                        </Descriptions.Item>
                        <Descriptions.Item label="Loading">
                            <Tag color={status.loading ? "blue" : "default"}>
                                {status.loading ? "Loading model" : "Idle"}
                            </Tag>
                        </Descriptions.Item>
                        <Descriptions.Item label="Model">
                            {status.model ?? "not loaded"}
                        </Descriptions.Item>
                    </Descriptions>
                )}
            </Card>
            <Card title="Examples per Category" className="settings-card">
                <Table<CategoryRow>
                    rowKey="name"
                    columns={columns}
                    dataSource={rows}
                    pagination={false}
                    locale={{ emptyText: "No categories available" }}
                />
            </Card>
            <Card title="Add Example" className="settings-card">
                <Form<{ category: string; text: string }>
                    form={addForm}
                    layout="inline"
                    onFinish={(values) => void onSubmitAdd(values)}
                >
                    <Form.Item
                        name="category"
                        label="Category"
                        initialValue={categories[0]}
                        rules={[{ required: true }]}
                    >
                        <Select options={categoryOptions} style={{ minWidth: 160 }} />
                    </Form.Item>
                    <Form.Item
                        name="text"
                        label="Example text"
                        style={{ flex: 1 }}
                        rules={[{ required: true, message: "Example text is required" }]}
                    >
                        <Input maxLength={500} placeholder="Sensitive example text" />
                    </Form.Item>
                    <Form.Item>
                        <Button type="primary" htmlType="submit" icon={<PlusOutlined />}>
                            Add
                        </Button>
                    </Form.Item>
                </Form>
            </Card>
            <Card title="Delete Example" className="settings-card">
                <Form<{ category: string; text: string }>
                    form={deleteForm}
                    layout="inline"
                    onFinish={(values) => void onSubmitDelete(values)}
                >
                    <Form.Item
                        name="category"
                        label="Category"
                        initialValue={categories[0]}
                        rules={[{ required: true }]}
                    >
                        <Select options={categoryOptions} style={{ minWidth: 160 }} />
                    </Form.Item>
                    <Form.Item
                        name="text"
                        label="Example text"
                        style={{ flex: 1 }}
                        rules={[{ required: true, message: "Example text is required" }]}
                    >
                        <Input maxLength={500} placeholder="Exact example text to remove" />
                    </Form.Item>
                    <Form.Item>
                        <Popconfirm
                            title="Delete this example?"
                            onConfirm={() => void deleteForm.submit()}
                        >
                            <Button danger htmlType="button" icon={<DeleteOutlined />}>
                                Delete
                            </Button>
                        </Popconfirm>
                    </Form.Item>
                </Form>
            </Card>
            <Typography.Paragraph type="secondary">
                Deleting requires the exact example text stored in the index. Use the per-category
                counts above to track the index state.
            </Typography.Paragraph>
        </div>
    );
}
