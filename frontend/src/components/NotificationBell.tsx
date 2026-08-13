import { ReactElement, useCallback, useState } from "react";
import { Badge, Button, Empty, List, Popover, Spin, Tag, Typography } from "antd";
import { BellOutlined, ReloadOutlined } from "@ant-design/icons";
import { useNavigate } from "react-router-dom";
import { useAppContext } from "../contexts/AppContext";
import { AuditEntry } from "../types";

function verdictColor(verdict: string | null | undefined): string {
    const value: string = String(verdict ?? "");
    return value === "BLOCK" ? "red" : value === "REVIEW" ? "orange" : "green";
}

function timeLabel(timestamp: string | undefined): string {
    if (timestamp === undefined || timestamp.length === 0) {
        return "";
    }
    return timestamp.slice(11, 19);
}

export function NotificationBell(): ReactElement {
    const { auditService } = useAppContext();
    const navigate = useNavigate();
    const [open, setOpen] = useState<boolean>(false);
    const [entries, setEntries] = useState<AuditEntry[]>([]);
    const [loading, setLoading] = useState<boolean>(false);

    const load = useCallback(async (): Promise<void> => {
        setLoading(true);
        try {
            const all: AuditEntry[] = await auditService.getAudit();
            setEntries(all.slice(0, 8));
        } catch {
            setEntries([]);
        } finally {
            setLoading(false);
        }
    }, [auditService]);

    const onOpenChange = (next: boolean): void => {
        setOpen(next);
        if (next) {
            void load();
        }
    };

    const content: ReactElement = (
        <div className="notification-bell__panel">
            <div className="notification-bell__header">
                <Typography.Text strong>Recent Activity</Typography.Text>
                <Button
                    type="text"
                    size="small"
                    icon={<ReloadOutlined />}
                    onClick={() => void load()}
                    aria-label="Refresh notifications"
                />
            </div>
            {loading ? (
                <div className="notification-bell__loading">
                    <Spin size="small" />
                </div>
            ) : entries.length === 0 ? (
                <Empty description="No recent moderation activity" />
            ) : (
                <List
                    size="small"
                    dataSource={entries}
                    locale={{ emptyText: "No recent moderation activity" }}
                    renderItem={(entry: AuditEntry): ReactElement => (
                        <List.Item>
                            <List.Item.Meta
                                title={
                                    <span className="notification-bell__title">
                                        <Tag color={verdictColor(entry.verdict)}>
                                            {String(entry.verdict ?? "-")}
                                        </Tag>
                                        <Typography.Text ellipsis>
                                            {entry.textPreview ?? entry.reason ?? "-"}
                                        </Typography.Text>
                                    </span>
                                }
                                description={timeLabel(entry.timestamp)}
                            />
                        </List.Item>
                    )}
                />
            )}
            <Button
                block
                type="link"
                onClick={() => {
                    setOpen(false);
                    navigate("/audit-log");
                }}
            >
                View Audit Log
            </Button>
        </div>
    );

    return (
        <Popover
            content={content}
            trigger="click"
            open={open}
            onOpenChange={onOpenChange}
            placement="bottomRight"
            arrow={false}
        >
            <Badge dot={entries.length > 0}>
                <Button type="text" icon={<BellOutlined />} aria-label="Notifications" />
            </Badge>
        </Popover>
    );
}
