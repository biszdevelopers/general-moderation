import { Navigate, createBrowserRouter } from "react-router-dom";
import { Layout } from "./components/Layout";
import { AuditLog } from "./pages/AuditLog";
import { Dashboard } from "./pages/Dashboard";
import { Export } from "./pages/Export";
import { ModelManagement } from "./pages/ModelManagement";
import { Phrases } from "./pages/Phrases";
import { Semantic } from "./pages/Semantic";
import { Settings } from "./pages/Settings";
import { TestWorkbench } from "./pages/TestWorkbench";
import { WordBank } from "./pages/WordBank";

export const router = createBrowserRouter([
  {
    path: "/",
    element: <Layout />,
    children: [
      { index: true, element: <Navigate to="/dashboard" replace /> },
      { path: "dashboard", element: <Dashboard /> },
      { path: "word-bank", element: <WordBank /> },
      { path: "phrases", element: <Phrases /> },
      { path: "semantic", element: <Semantic /> },
      { path: "audit-log", element: <AuditLog /> },
      { path: "export", element: <Export /> },
      { path: "models", element: <ModelManagement /> },
      { path: "settings", element: <Settings /> },
      { path: "test-workbench", element: <TestWorkbench /> },
    ],
  },
]);
