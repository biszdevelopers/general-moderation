import { Avatar, Breadcrumb, Button, Layout as AntdLayout, Menu, Typography } from "antd";
import {
    DashboardOutlined,
    DatabaseOutlined,
    ExportOutlined,
    FileSearchOutlined,
    LogoutOutlined,
    SettingOutlined,
    ToolOutlined,
    UserOutlined,
} from "@ant-design/icons";
import { Outlet, useLocation, useNavigate } from "react-router-dom";
import { ReactElement, useState } from "react";
import { useAppContext } from "../contexts/AppContext";
import { NotificationBell } from "./NotificationBell";

const { Header, Sider, Content, Footer } = AntdLayout;

const TITLES: Record<string, string> = {
    "/dashboard": "Dashboard",
    "/word-bank": "Word Bank",
    "/audit-log": "Audit Log",
    "/export": "Data Export",
    "/settings": "Settings",
    "/test-workbench": "Test Workbench",
};

export function Layout(): ReactElement {
    const navigate = useNavigate();
    const location = useLocation();
    const { logout } = useAppContext();
    const [collapsed, setCollapsed] = useState<boolean>(false);

    const selectedKey: string = location.pathname.startsWith("/word-bank")
        ? "/word-bank"
        : location.pathname.startsWith("/audit-log")
          ? "/audit-log"
          : location.pathname.startsWith("/export")
            ? "/export"
            : location.pathname.startsWith("/settings")
              ? "/settings"
              : location.pathname.startsWith("/test-workbench")
                ? "/test-workbench"
                : "/dashboard";

    const headerTitle: string = TITLES[selectedKey] ?? "General Moderation";

    return (
        <AntdLayout className="app-layout">
            <Sider
                className="app-sider"
                collapsible
                collapsed={collapsed}
                onCollapse={setCollapsed}
                width={224}
                breakpoint="lg"
                theme="light"
            >
                <div className="app-sider__brand">
                    <img
                        src="/logo.svg"
                        alt="General Moderation logo"
                        className="app-sider__logo"
                    />
                    {!collapsed && <span className="app-sider__name">General Moderation</span>}
                </div>
                <Menu
                    mode="inline"
                    selectedKeys={[selectedKey]}
                    onClick={(info) => navigate(info.key)}
                    items={[
                        { key: "/dashboard", icon: <DashboardOutlined />, label: "Dashboard" },
                        { key: "/word-bank", icon: <DatabaseOutlined />, label: "Word Bank" },
                        { key: "/audit-log", icon: <FileSearchOutlined />, label: "Audit Log" },
                        { key: "/export", icon: <ExportOutlined />, label: "Export" },
                        {
                            key: "/test-workbench",
                            icon: <ToolOutlined />,
                            label: "Test Workbench",
                        },
                        { key: "/settings", icon: <SettingOutlined />, label: "Settings" },
                    ]}
                />
            </Sider>
            <AntdLayout>
                <Header className="app-header">
                    <Typography.Text strong className="app-header__title">
                        {headerTitle}
                    </Typography.Text>
                    <div className="app-header__actions">
                        <NotificationBell />
                        <Avatar size="small" icon={<UserOutlined />} />
                        <Button type="text" icon={<LogoutOutlined />} onClick={logout}>
                            Sign Out
                        </Button>
                    </div>
                </Header>
                <Content className="app-content">
                    <Breadcrumb
                        className="app-breadcrumb"
                        items={[{ title: "General Moderation" }, { title: headerTitle }]}
                    />
                    <Outlet />
                </Content>
                <Footer className="app-footer">
                    General Moderation &middot; Multi-Language Content Moderation
                </Footer>
            </AntdLayout>
        </AntdLayout>
    );
}
