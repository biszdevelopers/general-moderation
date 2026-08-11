import { Avatar, Badge, Button, Layout as AntdLayout, Menu, Typography } from "antd";
import {
    BellOutlined,
    DashboardOutlined,
    DatabaseOutlined,
    FileSearchOutlined,
    LogoutOutlined,
    SettingOutlined,
    UserOutlined,
} from "@ant-design/icons";
import { Outlet, useLocation, useNavigate } from "react-router-dom";
import { ReactElement, useState } from "react";
import { useAppContext } from "../contexts/AppContext";

const { Header, Sider, Content, Footer } = AntdLayout;

export function Layout(): ReactElement {
    const navigate = useNavigate();
    const location = useLocation();
    const { logout } = useAppContext();
    const [collapsed, setCollapsed] = useState<boolean>(false);

    const selectedKey: string = location.pathname.startsWith("/word-bank")
        ? "/word-bank"
        : location.pathname.startsWith("/audit-log")
          ? "/audit-log"
          : location.pathname.startsWith("/settings")
            ? "/settings"
            : "/dashboard";

    return (
        <AntdLayout className="app-layout">
            <Sider
                className="app-sider"
                collapsible
                collapsed={collapsed}
                onCollapse={setCollapsed}
                width={220}
            >
                <div className="app-sider__brand">{collapsed ? "MA" : "Moderation Admin"}</div>
                <Menu
                    theme="dark"
                    mode="inline"
                    selectedKeys={[selectedKey]}
                    onClick={(info) => navigate(info.key)}
                    items={[
                        { key: "/dashboard", icon: <DashboardOutlined />, label: "Dashboard" },
                        { key: "/word-bank", icon: <DatabaseOutlined />, label: "Word Bank" },
                        { key: "/audit-log", icon: <FileSearchOutlined />, label: "Audit Log" },
                        { key: "/settings", icon: <SettingOutlined />, label: "Settings" },
                    ]}
                />
            </Sider>
            <AntdLayout>
                <Header className="app-header">
                    <Typography.Text strong className="app-header__title">
                        Multi-Language Moderation Console
                    </Typography.Text>
                    <div className="app-header__actions">
                        <Badge dot offset={[-6, 6]}>
                            <Button
                                type="text"
                                icon={<BellOutlined />}
                                aria-label="Notifications"
                            />
                        </Badge>
                        <Avatar size="small" icon={<UserOutlined />} />
                        <Button type="text" icon={<LogoutOutlined />} onClick={logout}>
                            Sign Out
                        </Button>
                    </div>
                </Header>
                <Content className="app-content">
                    <Outlet />
                </Content>
                <Footer className="app-footer">
                    General Moderation &middot; Multi-Language Content Moderation
                </Footer>
            </AntdLayout>
        </AntdLayout>
    );
}
