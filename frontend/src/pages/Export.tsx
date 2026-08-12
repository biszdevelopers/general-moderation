import { App as AntdApp, Alert, Button, Card, Descriptions, Space, Typography } from "antd";
import { CloudDownloadOutlined } from "@ant-design/icons";
import { useState } from "react";
import { ReactElement } from "react";
import { useAppContext } from "../contexts/AppContext";
import { LoadingSpinner } from "../components/LoadingSpinner";
import { LoginPrompt } from "../components/LoginPrompt";

const LAST_EXPORT_KEY: string = "moderation_last_export";

function saveBlob(blob: Blob, filename: string): void {
    const url: string = URL.createObjectURL(blob);
    const anchor: HTMLAnchorElement = document.createElement("a");
    anchor.href = url;
    anchor.download = filename;
    document.body.appendChild(anchor);
    anchor.click();
    anchor.remove();
    URL.revokeObjectURL(url);
}

export function Export(): ReactElement {
    const { exportService, authenticated } = useAppContext();
    const { message } = AntdApp.useApp();
    const [exporting, setExporting] = useState<boolean>(false);
    const [lastExport, setLastExport] = useState<string | null>(
        localStorage.getItem(LAST_EXPORT_KEY),
    );

    const onExport = async (): Promise<void> => {
        setExporting(true);
        try {
            const blob: Blob = await exportService.downloadExport();
            const stamp: string = new Date().toLocaleString();
            saveBlob(blob, `general_moderation_export_${Date.now()}.zip`);
            localStorage.setItem(LAST_EXPORT_KEY, stamp);
            setLastExport(stamp);
            message.success("Export archive downloaded");
        } catch (error: unknown) {
            message.error(String(error));
        } finally {
            setExporting(false);
        }
    };

    if (!authenticated) {
        return <LoginPrompt />;
    }

    return (
        <div className="page">
            <Typography.Title level={2} className="page__title">
                Data Export
            </Typography.Title>
            <Card title="Complete System Export" className="export-card">
                <Space direction="vertical" style={{ width: "100%" }} size="middle">
                    <Typography.Paragraph>
                        Downloads a ZIP archive with every SQLite database, a CSV dump of each
                        table, the audit logs, a redacted configuration snapshot, the semantic index
                        files, and an export metadata manifest.
                    </Typography.Paragraph>
                    <Space>
                        <Button
                            type="primary"
                            size="large"
                            icon={<CloudDownloadOutlined />}
                            loading={exporting}
                            onClick={() => void onExport()}
                        >
                            Export All Data
                        </Button>
                        {exporting && <LoadingSpinner />}
                    </Space>
                    {lastExport !== null && (
                        <Descriptions bordered size="small" column={1}>
                            <Descriptions.Item label="Last Export">{lastExport}</Descriptions.Item>
                        </Descriptions>
                    )}
                    <Alert
                        type="info"
                        message="The export endpoint is rate-limited to one request per ten minutes."
                    />
                </Space>
            </Card>
        </div>
    );
}
