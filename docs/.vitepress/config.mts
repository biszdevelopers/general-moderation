import { defineConfig } from "vitepress";
import { withMermaid } from "vitepress-plugin-mermaid";
import { katex } from "@mdit/plugin-katex";

export default defineConfig(
    withMermaid({
        title: "General Moderation",
        description:
            "Multi-language content moderation service with a 3-stage detection pipeline: fast-path rules, semantic similarity, user profiling, and a local LLM",
        lang: "en-US",
        lastUpdated: true,
        markdown: {
            config: (md) => {
                md.use(katex, { delimiters: "all" });
            },
        },
        themeConfig: {
            nav: [
                { text: "Guide", link: "/guide/" },
                { text: "Architecture", link: "/architecture/" },
                { text: "Algorithms", link: "/algorithms/" },
                { text: "API", link: "/api/" },
                { text: "Languages", link: "/languages/" },
                { text: "Contributing", link: "/contributing" },
            ],
            sidebar: {
                "/guide/": [
                    {
                        text: "Guide",
                        items: [
                            { text: "Overview", link: "/guide/" },
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
                            { text: "Overview", link: "/architecture/" },
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
                            { text: "Overview", link: "/algorithms/" },
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
                            { text: "Overview", link: "/api/" },
                            { text: "Public", link: "/api/public" },
                            { text: "Admin", link: "/api/admin" },
                        ],
                    },
                ],
                "/languages/": [
                    {
                        text: "Language Coverage",
                        items: [
                            { text: "Overview", link: "/languages/" },
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
    }),
);
