import { Navigate, createBrowserRouter } from "react-router-dom";
import { Layout } from "./components/Layout";
import { AuditLog } from "./pages/AuditLog";
import { Dashboard } from "./pages/Dashboard";
import { Export } from "./pages/Export";
import { Settings } from "./pages/Settings";
import { WordBank } from "./pages/WordBank";

export const router = createBrowserRouter([
    {
        path: "/",
        element: <Layout />,
        children: [
            { index: true, element: <Navigate to="/dashboard" replace /> },
            { path: "dashboard", element: <Dashboard /> },
            { path: "word-bank", element: <WordBank /> },
            { path: "audit-log", element: <AuditLog /> },
            { path: "export", element: <Export /> },
            { path: "settings", element: <Settings /> },
        ],
    },
]);
