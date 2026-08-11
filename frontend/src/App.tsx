import { App as AntdApp } from "antd";
import { RouterProvider } from "react-router-dom";
import { ReactElement } from "react";
import { AppProvider } from "./contexts/AppContext";
import { router } from "./router";

export function App(): ReactElement {
    return (
        <AntdApp>
            <AppProvider>
                <RouterProvider router={router} />
            </AppProvider>
        </AntdApp>
    );
}
