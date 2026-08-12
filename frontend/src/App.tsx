import { App as AntdApp, ConfigProvider, ThemeConfig } from "antd";
import { RouterProvider } from "react-router-dom";
import { ReactElement } from "react";
import { AppProvider } from "./contexts/AppContext";
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
            '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "PingFang SC", "Microsoft YaHei", sans-serif',
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

export function App(): ReactElement {
    return (
        <ConfigProvider theme={theme}>
            <AntdApp>
                <AppProvider>
                    <RouterProvider router={router} />
                </AppProvider>
            </AntdApp>
        </ConfigProvider>
    );
}
