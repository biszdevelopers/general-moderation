import { App as AntdApp, ConfigProvider, ThemeConfig, theme as antdTheme } from "antd";
import { RouterProvider } from "react-router-dom";
import { ReactElement } from "react";
import { AppProvider } from "./contexts/AppContext";
import { ThemeProvider, useTheme } from "./contexts/ThemeContext";
import { router } from "./router";

const theme: ThemeConfig = {
    token: {
        colorPrimary: "#2563eb",
        colorInfo: "#2563eb",
        colorLink: "#2563eb",
        colorSuccess: "#16a34a",
        colorWarning: "#d97706",
        colorError: "#dc2626",
        colorBgLayout: "#f1f5f9",
        colorTextBase: "#0f172a",
        colorTextSecondary: "#64748b",
        colorBorder: "#e2e8f0",
        colorBorderSecondary: "#e8edf3",
        borderRadius: 8,
        fontFamily:
            '"Noto Sans", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "PingFang SC", "Microsoft YaHei", sans-serif',
    },
    components: {
        Layout: {
            headerBg: "#ffffff",
            siderBg: "#ffffff",
            bodyBg: "#f1f5f9",
            headerHeight: 64,
        },
        Menu: {
            itemBg: "transparent",
            itemSelectedBg: "#eff6ff",
            itemSelectedColor: "#2563eb",
            itemHoverBg: "#f1f5f9",
            itemColor: "#475569",
            itemBorderRadius: 8,
            itemMarginInline: 8,
            activeBarBorderWidth: 0,
        },
        Card: {
            headerBg: "#ffffff",
            headerFontSize: 15,
            borderRadiusLG: 12,
            paddingLG: 20,
        },
        Table: {
            headerBg: "#f8fafc",
            headerColor: "#475569",
            headerSplitColor: "#e8edf3",
            borderColor: "#e8edf3",
        },
        Button: {
            borderRadius: 8,
            controlHeight: 36,
        },
        Input: {
            borderRadius: 8,
            controlHeight: 36,
        },
        InputNumber: {
            borderRadius: 8,
            controlHeight: 36,
        },
        Select: {
            borderRadius: 8,
            controlHeight: 36,
        },
        Modal: { borderRadiusLG: 12 },
    },
};

const darkTheme: ThemeConfig = {
    algorithm: antdTheme.darkAlgorithm,
    token: {
        colorPrimary: "#3b82f6",
        colorInfo: "#3b82f6",
        colorLink: "#60a5fa",
        colorSuccess: "#22c55e",
        colorWarning: "#f59e0b",
        colorError: "#ef4444",
        colorBgLayout: "#0f172a",
        colorTextBase: "#e2e8f0",
        colorTextSecondary: "#94a3b8",
        colorBorder: "#334155",
        colorBorderSecondary: "#1e293b",
        borderRadius: 8,
        fontFamily:
            '"Noto Sans", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "PingFang SC", "Microsoft YaHei", sans-serif',
    },
    components: {
        Layout: {
            headerBg: "#0f172a",
            siderBg: "#0f172a",
            bodyBg: "#0f172a",
            headerHeight: 64,
        },
        Menu: {
            itemBg: "transparent",
            itemSelectedBg: "#1e293b",
            itemSelectedColor: "#60a5fa",
            itemHoverBg: "#1e293b",
            itemColor: "#cbd5e1",
            itemBorderRadius: 8,
            itemMarginInline: 8,
            activeBarBorderWidth: 0,
        },
        Card: {
            headerBg: "#1e293b",
            headerFontSize: 15,
            borderRadiusLG: 12,
            paddingLG: 20,
        },
        Table: {
            headerBg: "#1e293b",
            headerColor: "#94a3b8",
            headerSplitColor: "#334155",
            borderColor: "#334155",
        },
        Button: {
            borderRadius: 8,
            controlHeight: 36,
        },
        Input: {
            borderRadius: 8,
            controlHeight: 36,
        },
        InputNumber: {
            borderRadius: 8,
            controlHeight: 36,
        },
        Select: {
            borderRadius: 8,
            controlHeight: 36,
        },
        Modal: { borderRadiusLG: 12 },
    },
};

function ThemedApp(): ReactElement {
    const { dark } = useTheme();
    return (
        <ConfigProvider theme={dark ? darkTheme : theme}>
            <AntdApp>
                <AppProvider>
                    <RouterProvider router={router} />
                </AppProvider>
            </AntdApp>
        </ConfigProvider>
    );
}

export function App(): ReactElement {
    return (
        <ThemeProvider>
            <ThemedApp />
        </ThemeProvider>
    );
}
