import {
    App as AntdApp,
    Button,
    Card,
    DatePicker,
    Input,
    List,
    Select,
    Space,
    Table,
    Tabs,
    Tag,
    Typography,
} from "antd";
import { TableProps } from "antd";
import { DownloadOutlined, SearchOutlined } from "@ant-design/icons";
import { useEffect, useMemo, useState } from "react";
import { ReactElement } from "react";
import { useAppContext } from "../contexts/AppContext";
import { AuditEntry, LogContent, LogFileInfo } from "../types";
import { LoadingSpinner } from "../components/LoadingSpinner";
import { LoginPrompt } from "../components/LoginPrompt";

function download(filename: string, content: string, mime: string): void {
    const blob: Blob = new Blob([content], { type: mime });
    const url: string = URL.createObjectURL(blob);
    const anchor: HTMLAnchorElement = document.createElement("a");
    anchor.href = url;
    anchor.download = filename;
    anchor.click();
    URL.revokeObjectURL(url);
}

function verdictTag(verdict: string | null | undefined): ReactElement {
    const value: string = String(verdict ?? "");
    const color: string = value === "BLOCK" ? "red" : value === "REVIEW" ? "orange" : "green";
    return <Tag color={color}>{value || "-"}</Tag>;
}

function toCsv(entries: AuditEntry[]): string {
    const headers: string[] = [
        "timestamp",
        "verdict",
        "levelUsed",
        "suspicionScore",
        "aiTriggered",
        "matchedWord",
        "matchedLanguage",
        "reason",
        "latencyMs",
        "textPreview",
        "userId",
        "requestId",
    ];
    const escape = (value: string | number | boolean | null | undefined): string => {
        const text: string = String(value ?? "");
        return `"${text.replace(/"/g, '""')}"`;
    };
    const rows: string[] = entries.map((entry) =>
        headers
            .map((header) => {
                const value: string | number | boolean | null | undefined = (
                    entry as Record<string, string | number | boolean | null | undefined>
                )[header];
                return escape(value);
            })
            .join(","),
    );
    return [headers.join(","), ...rows].join("\n");
}

export function AuditLog(): ReactElement {
    const { auditService, authenticated } = useAppContext();
    const { message } = AntdApp.useApp();
    const [entries, setEntries] = useState<AuditEntry[]>([]);
    const [logFiles, setLogFiles] = useState<LogFileInfo[]>([]);
    const [logContent, setLogContent] = useState<LogContent | null>(null);
    const [loading, setLoading] = useState<boolean>(true);
    const [verdictFilter, setVerdictFilter] = useState<string>("all");
    const [searchText, setSearchText] = useState<string>("");
    const [dateRange, setDateRange] = useState<[string, string] | null>(null);

    useEffect(() => {
        if (!authenticated) {
            setLoading(false);
            return;
        }
        const loadAll = async (): Promise<void> => {
            try {
                const [auditEntries, files] = await Promise.all([
                    auditService.getAudit(),
                    auditService.listLogs(),
                ]);
                setEntries(auditEntries);
                setLogFiles(files);
            } catch (error: unknown) {
                message.error(`Failed to load audit log: ${String(error)}`);
            } finally {
                setLoading(false);
            }
        };
        void loadAll();
    }, [auditService, message, authenticated]);

    const viewLog = async (filename: string): Promise<void> => {
        try {
            setLogContent(await auditService.getLog(filename));
        } catch (error: unknown) {
            message.error(String(error));
        }
    };

    const filteredEntries: AuditEntry[] = useMemo(() => {
        const query: string = searchText.trim().toLowerCase();
        return entries.filter((entry) => {
            if (verdictFilter !== "all" && entry.verdict !== verdictFilter) {
                return false;
            }
            if (query.length > 0) {
                const haystack: string = [
                    entry.textPreview,
                    entry.reason,
                    entry.matchedWord,
                    entry.userId,
                    entry.requestId,
                    entry.matchedLanguage,
                ]
                    .map((value) => String(value ?? ""))
                    .join(" ")
                    .toLowerCase();
                if (!haystack.includes(query)) {
                    return false;
                }
            }
            if (dateRange !== null) {
                const day: string = entry.timestamp?.slice(0, 10) ?? "";
                if (day < dateRange[0] || day > dateRange[1]) {
                    return false;
                }
            }
            return true;
        });
    }, [entries, verdictFilter, searchText, dateRange]);

    const onExport = (): void => {
        download("audit-log.csv", toCsv(filteredEntries), "text/csv");
        message.success(`Exported ${filteredEntries.length} audit records`);
    };

    const columns: TableProps<AuditEntry>["columns"] = [
        { title: "Timestamp", dataIndex: "timestamp", key: "timestamp", width: 160 },
        { title: "Verdict", dataIndex: "verdict", key: "verdict", render: verdictTag },
        {
            title: "Level",
            dataIndex: "levelUsed",
            key: "levelUsed",
            render: (value: unknown): ReactElement => (
                <Tag color={value === 2 ? "blue" : "default"}>{String(value ?? "-")}</Tag>
            ),
        },
        {
            title: "AI",
            dataIndex: "aiTriggered",
            key: "aiTriggered",
            render: (value: unknown): ReactElement =>
                value ? (
                    <Tag color="purple">LLM</Tag>
                ) : (
                    <Typography.Text type="secondary">-</Typography.Text>
                ),
        },
        {
            title: "Score",
            dataIndex: "suspicionScore",
            key: "suspicionScore",
            render: (value: unknown): string => {
                const numeric: number = Number(value);
                return Number.isFinite(numeric) ? numeric.toFixed(1) : "-";
            },
        },
        { title: "Text Preview", dataIndex: "textPreview", key: "textPreview", ellipsis: true },
        { title: "Matched Word", dataIndex: "matchedWord", key: "matchedWord" },
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

    if (!authenticated) {
        return <LoginPrompt />;
    }

    if (loading) {
        return <LoadingSpinner />;
    }

    return (
        <div className="page">
            <Typography.Title level={2} className="page__title">
                Audit Log
            </Typography.Title>
            <Typography.Paragraph className="page__subtitle">
                Review recent moderation decisions and inspect the JSONL log files.
            </Typography.Paragraph>
            <Tabs
                items={[
                    {
                        key: "entries",
                        label: "Audit Entries",
                        children: (
                            <>
                                <Space wrap className="audit-toolbar">
                                    <Select
                                        value={verdictFilter}
                                        onChange={setVerdictFilter}
                                        style={{ width: 160 }}
                                        options={[
                                            { value: "all", label: "All Verdicts" },
                                            { value: "BLOCK", label: "BLOCK" },
                                            { value: "REVIEW", label: "REVIEW" },
                                            { value: "PASS", label: "PASS" },
                                        ]}
                                    />
                                    <DatePicker.RangePicker
                                        onChange={(_, dateStrings: string[]) =>
                                            setDateRange(
                                                dateStrings[0] && dateStrings[1]
                                                    ? [dateStrings[0], dateStrings[1]]
                                                    : null,
                                            )
                                        }
                                    />
                                    <Button icon={<DownloadOutlined />} onClick={onExport}>
                                        Export CSV
                                    </Button>
                                </Space>
                                <Input
                                    allowClear
                                    value={searchText}
                                    onChange={(event) => setSearchText(event.target.value)}
                                    placeholder="Search preview, reason, word, user..."
                                    prefix={<SearchOutlined />}
                                    className="audit-search"
                                    aria-label="Filter audit records"
                                />
                                <Table<AuditEntry>
                                    rowKey={(entry: AuditEntry, index?: number): string =>
                                        `${String(index ?? 0)}-${String(entry.timestamp ?? "")}`
                                    }
                                    columns={columns}
                                    dataSource={filteredEntries}
                                    pagination={{
                                        pageSize: 20,
                                        showTotal: (total) => `${total} records`,
                                    }}
                                    scroll={{ x: "max-content" }}
                                    locale={{
                                        emptyText: "No audit records match the current filters",
                                    }}
                                />
                            </>
                        ),
                    },
                    {
                        key: "files",
                        label: "Log Files",
                        children: (
                            <div className="log-files">
                                <List
                                    dataSource={logFiles}
                                    renderItem={(file: LogFileInfo): ReactElement => (
                                        <List.Item
                                            actions={[
                                                <Button
                                                    key="view"
                                                    onClick={() => void viewLog(file.name)}
                                                >
                                                    View Tail
                                                </Button>,
                                            ]}
                                        >
                                            <List.Item.Meta
                                                title={file.name}
                                                description={`${file.size} bytes`}
                                            />
                                        </List.Item>
                                    )}
                                />
                                {logContent !== null && (
                                    <Card
                                        title={`${logContent.name} (${logContent.lines} lines)`}
                                        className="log-files__preview"
                                    >
                                        <pre className="log-files__content">
                                            {logContent.tail.join("\n")}
                                        </pre>
                                    </Card>
                                )}
                            </div>
                        ),
                    },
                ]}
            />
        </div>
    );
}
