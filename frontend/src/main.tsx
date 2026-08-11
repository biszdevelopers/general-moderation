import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import { App } from "./App";
import "./styles/global.css";
import "./styles/layout.css";
import "./styles/components.css";

const container: HTMLElement | null = document.getElementById("root");
if (container === null) {
    throw new Error("Root element not found");
}

createRoot(container).render(
    <StrictMode>
        <App />
    </StrictMode>,
);
