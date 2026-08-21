import { Avatar, Breadcrumb, Button, Layout as AntdLayout, Menu, Typography } from "antd";
import {
  AlertOutlined,
  CloudServerOutlined,
  DashboardOutlined,
  DatabaseOutlined,
  ExportOutlined,
  FileSearchOutlined,
  LogoutOutlined,
  MoonOutlined,
  NodeIndexOutlined,
  SettingOutlined,
  SunOutlined,
  ToolOutlined,
  UserOutlined,
} from "@ant-design/icons";
import { Outlet, useLocation, useNavigate } from "react-router-dom";
import { ReactElement, useState } from "react";
import { useAppContext } from "../contexts/AppContext";
import { useTheme } from "../contexts/ThemeContext";
import { NotificationBell } from "./NotificationBell";

const { Header, Sider, Content, Footer } = AntdLayout;

const TITLES: Record<string, string> = {
  "/dashboard": "Dashboard",
  "/word-bank": "Word Bank",
  "/phrases": "Critical Phrases",
  "/semantic": "Semantic Index",
  "/audit-log": "Audit Log",
  "/export": "Data Export",
  "/models": "Model Management",
  "/settings": "Settings",
  "/test-workbench": "Test Workbench",
};

export function Layout(): ReactElement {
  const navigate = useNavigate();
  const location = useLocation();
  const { logout } = useAppContext();
  const { dark, toggleDark } = useTheme();
  const [collapsed, setCollapsed] = useState<boolean>(false);

  const selectedKey: string = location.pathname.startsWith("/word-bank")
    ? "/word-bank"
    : location.pathname.startsWith("/phrases")
      ? "/phrases"
      : location.pathname.startsWith("/semantic")
        ? "/semantic"
        : location.pathname.startsWith("/audit-log")
          ? "/audit-log"
          : location.pathname.startsWith("/export")
            ? "/export"
            : location.pathname.startsWith("/models")
              ? "/models"
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
        collapsedWidth={0}
        theme="light"
      >
        <div className="app-sider__brand">
          <img src="/logo.svg" alt="General Moderation logo" className="app-sider__logo" />
          {!collapsed && <span className="app-sider__name">General Moderation</span>}
        </div>
        <Menu
          mode="inline"
          selectedKeys={[selectedKey]}
          onClick={(info) => navigate(info.key)}
          items={[
            { key: "/dashboard", icon: <DashboardOutlined />, label: "Dashboard" },
            { key: "/word-bank", icon: <DatabaseOutlined />, label: "Word Bank" },
            { key: "/phrases", icon: <AlertOutlined />, label: "Critical Phrases" },
            { key: "/semantic", icon: <NodeIndexOutlined />, label: "Semantic Index" },
            { key: "/audit-log", icon: <FileSearchOutlined />, label: "Audit Log" },
            { key: "/export", icon: <ExportOutlined />, label: "Export" },
            {
              key: "/models",
              icon: <CloudServerOutlined />,
              label: "Models",
            },
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
            <Button
              type="text"
              icon={dark ? <SunOutlined /> : <MoonOutlined />}
              onClick={toggleDark}
              aria-label={dark ? "Switch to light mode" : "Switch to dark mode"}
              title={dark ? "Switch to light mode" : "Switch to dark mode"}
            />
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
