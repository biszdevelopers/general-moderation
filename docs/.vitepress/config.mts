import { defineConfig } from "vitepress";

export default defineConfig({
    title: "Moderation Service",
    description:
        "Production-grade multi-language content moderation microservice with a C/C++/Rust detection pipeline",
    lang: "en-US",
    lastUpdated: true,
    themeConfig: {
        nav: [
            { text: "Guide", link: "/guide/getting-started" },
            { text: "API", link: "/api/index" },
            { text: "Languages", link: "/languages/index" },
            { text: "Contributing", link: "/contributing" },
        ],
        sidebar: {
            "/guide/": [
                {
                    text: "Guide",
                    items: [
                        { text: "Getting Started", link: "/guide/getting-started" },
                        { text: "Configuration", link: "/guide/configuration" },
                        { text: "Word Banks", link: "/guide/wordbanks" },
                        { text: "Security", link: "/guide/security" },
                        { text: "Deployment", link: "/guide/deployment" },
                    ],
                },
            ],
            "/api/": [
                {
                    text: "API Reference",
                    items: [
                        { text: "Overview", link: "/api/index" },
                        { text: "Moderation", link: "/api/moderation" },
                        { text: "Admin", link: "/api/admin" },
                    ],
                },
            ],
            "/languages/": [
                {
                    text: "Language Coverage",
                    items: [
                        { text: "Overview", link: "/languages/index" },
                        { text: "English", link: "/languages/en" },
                        { text: "Simplified Chinese", link: "/languages/zh-CN" },
                        { text: "Traditional Chinese", link: "/languages/zh-TW" },
                        { text: "Japanese", link: "/languages/ja" },
                        { text: "Korean", link: "/languages/ko" },
                        { text: "Russian", link: "/languages/ru" },
                        { text: "German", link: "/languages/de" },
                        { text: "Italian", link: "/languages/it" },
                        { text: "Spanish", link: "/languages/es" },
                        { text: "French", link: "/languages/fr" },
                        { text: "Arabic", link: "/languages/ar" },
                        { text: "Hindi", link: "/languages/hi" },
                        { text: "Turkish", link: "/languages/tr" },
                        { text: "Portuguese", link: "/languages/pt" },
                    ],
                },
            ],
        },
    },
});
