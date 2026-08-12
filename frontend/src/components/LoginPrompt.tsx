import { App as AntdApp, Button, Card, Input, Space, Typography } from "antd";
import { KeyOutlined } from "@ant-design/icons";
import { useState } from "react";
import { ReactElement } from "react";
import { useAppContext } from "../contexts/AppContext";

export function LoginPrompt(): ReactElement {
    const { login } = useAppContext();
    const { message } = AntdApp.useApp();
    const [apiKey, setApiKey] = useState<string>("");

    const onSave = (): void => {
        const key: string = apiKey.trim();
        if (key.length === 0) {
            message.warning("Paste your admin API key to continue");
            return;
        }
        login(key);
        message.success("API key saved");
    };

    return (
        <div className="page">
            <Typography.Title level={2} className="page__title">
                Administrator Login
            </Typography.Title>
            <Typography.Paragraph className="page__subtitle">
                Authenticate to continue.
            </Typography.Paragraph>
            <Card className="settings-card">
                <Space direction="vertical" style={{ width: "100%" }} size="middle">
                    <Typography.Paragraph>
                        This page requires the administrator API key (the{" "}
                        <Typography.Text code>ADMIN_API_KEY</Typography.Text> from{" "}
                        <Typography.Text code>backend/.env</Typography.Text>). Paste it below to
                        continue.
                    </Typography.Paragraph>
                    <Input.Password
                        prefix={<KeyOutlined />}
                        placeholder="Admin API key"
                        value={apiKey}
                        onChange={(event) => setApiKey(event.target.value)}
                        onPressEnter={onSave}
                    />
                    <Button type="primary" onClick={onSave}>
                        Save Key
                    </Button>
                </Space>
            </Card>
        </div>
    );
}
