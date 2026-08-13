/// <reference types="vitest/config" />
import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

export default defineConfig({
    plugins: [react()],
    build:{
        rolldownOptions:{
            output:{
                codeSplitting: true
            }
        }
    },
    test: {
        environment: "jsdom",
        include: ["src/**/*.test.ts"],
    },
    server: {
        host: "127.0.0.1",
        port: 5173,
        proxy: {
            "/admin": {
                target: "http://127.0.0.1:8080",
                changeOrigin: true,
            },
            "/test": {
                target: "http://127.0.0.1:8080",
                changeOrigin: true,
            },
            "/moderate": {
                target: "http://127.0.0.1:8080",
                changeOrigin: true,
            },
            "/health": {
                target: "http://127.0.0.1:8080",
                changeOrigin: true,
            },
            "/metrics": {
                target: "http://127.0.0.1:8080",
                changeOrigin: true,
            },
        },
    },
});
