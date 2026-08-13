import { ReactElement, useState } from "react";
import {
    App as AntdApp,
    Button,
    Card,
    Col,
    Input,
    Row,
    Select,
    Space,
    Tabs,
    Typography,
} from "antd";
import { PlayCircleOutlined, ThunderboltOutlined } from "@ant-design/icons";
import { useAppContext } from "../contexts/AppContext";
import { useSseStream } from "../hooks/useSseStream";
import { ModerateDetailResult } from "../types";
import { ConfigPlayground } from "./TestWorkbench/ConfigPlayground";
import { DashboardPanel } from "./TestWorkbench/DashboardPanel";
import { LoadTestPanel } from "./TestWorkbench/LoadTestPanel";
import { PipelineVisualization } from "./TestWorkbench/PipelineVisualization";
import { UserProfileViewer } from "./TestWorkbench/UserProfileViewer";

const APP_OPTIONS: { value: string; label: string }[] = [
    { value: "default", label: "default" },
    { value: "web", label: "web" },
    { value: "mobile", label: "mobile" },
    { value: "forum", label: "forum" },
];

export function TestWorkbench(): ReactElement {
    const { testApiService } = useAppContext();
    const { message } = AntdApp.useApp();
    const { running, events, error, start, reset } = useSseStream();
    const [text, setText] = useState<string>("");
    const [userId, setUserId] = useState<string>("");
    const [appName, setAppName] = useState<string>("default");
    const [result, setResult] = useState<ModerateDetailResult | null>(null);

    const onModerate = async (): Promise<void> => {
        if (text.trim().length === 0) {
            message.warning("Enter a message to moderate");
            return;
        }
        setResult(null);
        reset();
        const payload: { text: string; user_id: string; app_name: string } = {
            text,
            user_id: userId.trim() || `wb-${Date.now().toString(36)}`,
            app_name: appName,
        };
        const streamResult = await start((onEvent) =>
            testApiService.moderateDetail(payload, onEvent),
        );
        if (streamResult !== null) {
            setResult(streamResult as ModerateDetailResult);
        }
    };

    const onSample = (): void => {
        setText("I will kill you tonight");
    };

    return (
        <div className="page">
            <Typography.Title level={2} className="page__title">
                Test Workbench
            </Typography.Title>
            <Typography.Paragraph className="page__subtitle">
                Run the moderation pipeline live, inspect every detector, load-test concurrency, and
                tune runtime settings.
            </Typography.Paragraph>
            <Card className="workbench-card">
                <Space direction="vertical" style={{ width: "100%" }} size="middle">
                    <Row gutter={[12, 12]}>
                        <Col xs={24} lg={16}>
                            <Input.TextArea
                                rows={3}
                                value={text}
                                onChange={(event) => setText(event.target.value)}
                                placeholder="Paste any message to moderate..."
                                maxLength={8192}
                            />
                        </Col>
                        <Col xs={24} lg={8}>
                            <Space direction="vertical" style={{ width: "100%" }}>
                                <Input
                                    addonBefore="User ID"
                                    value={userId}
                                    onChange={(event) => setUserId(event.target.value)}
                                    placeholder="auto-generated if empty"
                                />
                                <Select
                                    value={appName}
                                    onChange={setAppName}
                                    options={APP_OPTIONS}
                                    style={{ width: "100%" }}
                                    placeholder="App name"
                                />
                            </Space>
                        </Col>
                    </Row>
                    <Space>
                        <Button
                            type="primary"
                            size="large"
                            icon={<ThunderboltOutlined />}
                            loading={running}
                            onClick={() => void onModerate()}
                        >
                            Moderate
                        </Button>
                        <Button size="large" icon={<PlayCircleOutlined />} onClick={onSample}>
                            Sample Message
                        </Button>
                    </Space>
                </Space>
            </Card>
            {error !== null && (
                <Card className="workbench-card">
                    <Typography.Text type="danger">{error}</Typography.Text>
                </Card>
            )}
            <Tabs
                className="workbench-tabs"
                defaultActiveKey="moderate"
                items={[
                    {
                        key: "moderate",
                        label: "Interactive Test",
                        children: (
                            <PipelineVisualization
                                events={events}
                                result={result}
                                running={running}
                            />
                        ),
                    },
                    {
                        key: "load",
                        label: "Load Test",
                        children: <LoadTestPanel />,
                    },
                    {
                        key: "config",
                        label: "Configuration",
                        children: <ConfigPlayground />,
                    },
                    {
                        key: "users",
                        label: "User Profiles",
                        children: <UserProfileViewer />,
                    },
                    {
                        key: "dashboard",
                        label: "Dashboard",
                        children: <DashboardPanel />,
                    },
                ]}
            />
        </div>
    );
}
