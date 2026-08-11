import { defineConfig } from "vitepress";

export default defineConfig({
    title: "General Moderation",
    description:
        "Multi-language content moderation service with a 3-stage detection pipeline: fast-path rules, semantic similarity, user profiling, and a local LLM",
    lang: "en-US",
    lastUpdated: true,
    themeConfig: {
        nav: [
            { text: "Guide", link: "/guide/getting-started" },
            { text: "Architecture", link: "/architecture/index" },
            { text: "Algorithms", link: "/algorithms/index" },
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
                        { text: "Admin Settings", link: "/guide/admin-settings" },
                        { text: "Data Export", link: "/guide/data-export" },
                        { text: "Security", link: "/guide/security" },
                        { text: "Deployment", link: "/guide/deployment" },
                    ],
                },
            ],
            "/architecture/": [
                {
                    text: "Architecture",
                    items: [
                        { text: "Overview", link: "/architecture/index" },
                        { text: "3-Stage Pipeline", link: "/architecture/pipeline" },
                        { text: "Data Flow", link: "/architecture/data-flow" },
                        { text: "Archive Strategy", link: "/architecture/archive-strategy" },
                    ],
                },
            ],
            "/algorithms/": [
                {
                    text: "Algorithms",
                    items: [
                        { text: "Overview", link: "/algorithms/index" },
                        { text: "Aho-Corasick", link: "/algorithms/aho-corasick" },
                        { text: "BK-Tree", link: "/algorithms/bk-tree" },
                        { text: "Metaphone", link: "/algorithms/metaphone" },
                        { text: "Semantic Similarity", link: "/algorithms/semantic-similarity" },
                        { text: "Suspicion Score", link: "/algorithms/suspicion-score" },
                        { text: "User Profiling", link: "/algorithms/user-profiling" },
                        { text: "Weight Tuning", link: "/algorithms/weight-tuning" },
                    ],
                },
            ],
            "/api/": [
                {
                    text: "API Reference",
                    items: [
                        { text: "Overview", link: "/api/index" },
                        { text: "Public", link: "/api/public" },
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
