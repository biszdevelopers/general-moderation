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
    server: {
        host: "127.0.0.1",
        port: 5173,
        proxy: {
            "/admin": {
                target: "http://127.0.0.1:8080",
                changeOrigin: true,
            },
        },
    },
});
