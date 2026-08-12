import { App as AntdApp, Button, Card, List, Table, Tabs, Typography } from "antd";
import { TableProps } from "antd";
import { useEffect, useState } from "react";
import { ReactElement } from "react";
import { useAppContext } from "../contexts/AppContext";
import { AuditEntry, LogContent, LogFileInfo } from "../types";
import { LoadingSpinner } from "../components/LoadingSpinner";
import { LoginPrompt } from "../components/LoginPrompt";

export function AuditLog(): ReactElement {
    const { auditService, authenticated } = useAppContext();
    const { message } = AntdApp.useApp();
    const [entries, setEntries] = useState<AuditEntry[]>([]);
    const [logFiles, setLogFiles] = useState<LogFileInfo[]>([]);
    const [logContent, setLogContent] = useState<LogContent | null>(null);
    const [loading, setLoading] = useState<boolean>(true);

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

    const columns: TableProps<AuditEntry>["columns"] = [
        { title: "Timestamp", dataIndex: "timestamp", key: "timestamp" },
        { title: "Level", dataIndex: "level", key: "level" },
        { title: "Verdict", dataIndex: "verdict", key: "verdict" },
        { title: "Level Used", dataIndex: "levelUsed", key: "levelUsed" },
        { title: "Text Preview", dataIndex: "textPreview", key: "textPreview" },
        { title: "Matched Word", dataIndex: "matchedWord", key: "matchedWord" },
        {
            title: "Latency (ms)",
            dataIndex: "latencyMs",
            key: "latencyMs",
            render: (value: number | undefined): string =>
                value !== undefined ? value.toFixed(2) : "",
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
                            <Table<AuditEntry>
                                rowKey={(entry: AuditEntry, index?: number): string =>
                                    `${String(index ?? 0)}-${String(entry.timestamp ?? "")}`
                                }
                                columns={columns}
                                dataSource={entries}
                                pagination={{ pageSize: 20 }}
                            />
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
