import { ReactElement, useState } from "react";
import {
    App as AntdApp,
    Button,
    Card,
    Col,
    Input,
    Row,
    Space,
    Statistic,
    Table,
    TableProps,
    Tag,
    Tooltip,
    Typography,
} from "antd";
import { ReloadOutlined, SearchOutlined } from "@ant-design/icons";
import { useAppContext } from "../../contexts/AppContext";
import { UserDailyRow, UserProfile } from "../../types";

function RatioChart(props: { daily: UserDailyRow[] }): ReactElement {
    const { daily } = props;
    if (daily.length === 0) {
        return <Typography.Text type="secondary">No daily history recorded yet.</Typography.Text>;
    }
    const maxTotal: number = Math.max(1, ...daily.map((row) => row.total_msgs));
    return (
        <div className="ratio-chart">
            {daily.map((row) => {
                const ratio: number = row.total_msgs > 0 ? row.flagged_msgs / row.total_msgs : 0;
                const height: number = Math.max(2, (row.total_msgs / maxTotal) * 90);
                return (
                    <Tooltip
                        key={row.date}
                        title={`${row.date}: ${row.flagged_msgs}/${row.total_msgs} flagged (${(ratio * 100).toFixed(0)}%)`}
                    >
                        <div className="ratio-chart__col" style={{ height: `${height}%` }}>
                            <div
                                className="ratio-chart__bar"
                                style={{
                                    backgroundColor:
                                        ratio > 0.5
                                            ? "#dc2626"
                                            : ratio > 0.2
                                              ? "#d97706"
                                              : "#16a34a",
                                }}
                            />
                            <div className="ratio-chart__label">{row.date.slice(5)}</div>
                        </div>
                    </Tooltip>
                );
            })}
        </div>
    );
}

export function UserProfileViewer(): ReactElement {
    const { testApiService } = useAppContext();
    const { message } = AntdApp.useApp();
    const [appName, setAppName] = useState<string>("default");
    const [userId, setUserId] = useState<string>("");
    const [profile, setProfile] = useState<UserProfile | null>(null);
    const [loading, setLoading] = useState<boolean>(false);
    const [seeding, setSeeding] = useState<boolean>(false);

    const loadProfile = async (): Promise<void> => {
        if (userId.trim().length === 0) {
            message.warning("Enter a user ID");
            return;
        }
        setLoading(true);
        try {
            setProfile(
                await testApiService.getUserProfile(appName.trim() || "default", userId.trim()),
            );
        } catch (err: unknown) {
            message.error(`Failed to load profile: ${String(err)}`);
        } finally {
            setLoading(false);
        }
    };

    const onSeed = async (total: number, flagged: number): Promise<void> => {
        if (userId.trim().length === 0) {
            message.warning("Enter a user ID first");
            return;
        }
        setSeeding(true);
        try {
            await testApiService.seedUserProfile(
                appName.trim() || "default",
                userId.trim(),
                total,
                flagged,
            );
            message.success(`Seeded ${total} messages (${flagged} flagged)`);
            await loadProfile();
        } catch (err: unknown) {
            message.error(`Seeding failed: ${String(err)}`);
        } finally {
            setSeeding(false);
        }
    };

    const columns: TableProps<UserDailyRow>["columns"] = [
        { title: "Date", dataIndex: "date", key: "date" },
        { title: "Messages", dataIndex: "total_msgs", key: "total_msgs" },
        { title: "Flagged", dataIndex: "flagged_msgs", key: "flagged_msgs" },
        { title: "Blocked", dataIndex: "blocked_msgs", key: "blocked_msgs" },
        { title: "Reviewed", dataIndex: "reviewed_msgs", key: "reviewed_msgs" },
        {
            title: "Ratio",
            key: "ratio",
            render: (_: unknown, row: UserDailyRow) => {
                const ratio: number = row.total_msgs > 0 ? row.flagged_msgs / row.total_msgs : 0;
                return (
                    <Tag color={ratio > 0.5 ? "red" : ratio > 0.2 ? "orange" : "green"}>
                        {(ratio * 100).toFixed(0)}%
                    </Tag>
                );
            },
        },
    ];

    return (
        <Card title="User Profile Viewer" className="workbench-card">
            <Space direction="vertical" style={{ width: "100%" }} size="large">
                <Space wrap>
                    <Input
                        addonBefore="App"
                        value={appName}
                        onChange={(event) => setAppName(event.target.value)}
                        style={{ width: 180 }}
                        placeholder="default"
                    />
                    <Input
                        addonBefore="User ID"
                        value={userId}
                        onChange={(event) => setUserId(event.target.value)}
                        style={{ width: 240 }}
                        placeholder="user-123"
                    />
                    <Button
                        type="primary"
                        icon={<SearchOutlined />}
                        loading={loading}
                        onClick={() => void loadProfile()}
                    >
                        Load Profile
                    </Button>
                </Space>
                <Space wrap>
                    <Button disabled={seeding} onClick={() => void onSeed(0, 0)}>
                        Simulate New User
                    </Button>
                    <Button disabled={seeding} onClick={() => void onSeed(50, 1)}>
                        Simulate Known Good
                    </Button>
                    <Button disabled={seeding} onClick={() => void onSeed(50, 40)}>
                        Simulate Known Bad
                    </Button>
                </Space>
                {profile === null ? (
                    <Typography.Text type="secondary">
                        Load or seed a user profile to inspect its history and bad-content ratio.
                    </Typography.Text>
                ) : (
                    <>
                        <Row gutter={[16, 16]}>
                            <Col xs={12} md={6}>
                                <Statistic title="Total Messages" value={profile.total_msgs} />
                            </Col>
                            <Col xs={12} md={6}>
                                <Statistic title="Flagged" value={profile.flagged_msgs} />
                            </Col>
                            <Col xs={12} md={6}>
                                <Statistic title="Blocked" value={profile.blocked_msgs} />
                            </Col>
                            <Col xs={12} md={6}>
                                <Statistic
                                    title="Bad Ratio"
                                    value={profile.ratio}
                                    precision={3}
                                    valueStyle={{
                                        color:
                                            profile.ratio > 0.5
                                                ? "#dc2626"
                                                : profile.ratio > 0.2
                                                  ? "#d97706"
                                                  : "#16a34a",
                                    }}
                                />
                            </Col>
                        </Row>
                        <Card size="small" title="Ratio Over Time (rolling window)">
                            <RatioChart daily={profile.daily} />
                        </Card>
                        <Card size="small" title="Daily History">
                            <Table<UserDailyRow>
                                rowKey="date"
                                size="small"
                                columns={columns}
                                dataSource={profile.daily}
                                pagination={false}
                                locale={{ emptyText: "No daily rows yet" }}
                            />
                        </Card>
                        {profile.summaries.length > 0 && (
                            <Card size="small" title="Archived Cycles">
                                <Space wrap>
                                    {profile.summaries.map((summary) => (
                                        <Tag key={summary.cycle_id}>
                                            Cycle {summary.cycle_id}: {summary.total_msgs} msgs,{" "}
                                            {summary.flagged_msgs} flagged
                                        </Tag>
                                    ))}
                                </Space>
                            </Card>
                        )}
                        <Space>
                            <Button icon={<ReloadOutlined />} onClick={() => void loadProfile()}>
                                Refresh
                            </Button>
                        </Space>
                    </>
                )}
            </Space>
        </Card>
    );
}
