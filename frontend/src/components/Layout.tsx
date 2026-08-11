import { Layout as AntdLayout, Menu, Typography, Button } from "antd";
import {
    DashboardOutlined,
    DatabaseOutlined,
    FileSearchOutlined,
    LogoutOutlined,
    SettingOutlined,
} from "@ant-design/icons";
import { Outlet, useLocation, useNavigate } from "react-router";
import { ReactElement } from "react";
import { useAppContext } from "../contexts/AppContext";

const { Header, Sider, Content } = AntdLayout;

export function Layout(): ReactElement {
    const navigate = useNavigate();
    const location = useLocation();
    const { logout } = useAppContext();

    const selectedKey: string = location.pathname.startsWith("/word-bank")
        ? "/word-bank"
        : location.pathname.startsWith("/audit-log")
            ? "/audit-log"
            : location.pathname.startsWith("/settings")
                ? "/settings"
                : "/dashboard";

    const onMenuClick = (key: string): void => {
        navigate(key);
    };

    const onLogout = (): void => {
        logout();
    };

    return (
        <AntdLayout className="app-layout">
            <Sider className="app-sider" width={220}>
                <div className="app-sider__brand">Moderation Admin</div>
                <Menu
                    theme="dark"
                    mode="inline"
                    selectedKeys={[selectedKey]}
                    onClick={(info) => onMenuClick(info.key)}
                    items={[
                        {
                            key: "/dashboard",
                            icon: <DashboardOutlined />,
                            label: "Dashboard",
                        },
                        {
                            key: "/word-bank",
                            icon: <DatabaseOutlined />,
                            label: "Word Bank",
                        },
                        {
                            key: "/audit-log",
                            icon: <FileSearchOutlined />,
                            label: "Audit Log",
                        },
                        {
                            key: "/settings",
                            icon: <SettingOutlined />,
                            label: "Settings",
                        },
                    ]}
                />
            </Sider>
            <AntdLayout>
                <Header className="app-header">
                    <Typography.Text strong className="app-header__title">
                        Multi-Language Moderation Console
                    </Typography.Text>
                    <Button
                        type="text"
                        icon={<LogoutOutlined />}
                        onClick={onLogout}
                        className="app-header__logout"
                    >
                        Sign Out
                    </Button>
                </Header>
                <Content className="app-content">
                    <Outlet />
                </Content>
            </AntdLayout>
        </AntdLayout>
    );
}
