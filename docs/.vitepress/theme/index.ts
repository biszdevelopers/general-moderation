import { onMounted } from "vue";
import DefaultTheme from "vitepress/theme";
import type { Theme } from "vitepress";
import "katex/dist/katex.min.css";
import "./custom.css";

function enableMermaidZoom(): void {
    const toggle = (event: Event): void => {
        const target = event.target as HTMLElement | null;
        if (!target || !target.closest(".mermaid svg")) return;
        const svg = target.closest(".mermaid svg") as SVGSVGElement | null;
        if (!svg) return;
        svg.classList.toggle("zoomed");
        const container = svg.closest(".mermaid") as HTMLElement | null;
        if (container && svg.classList.contains("zoomed")) {
            const rect = svg.getBoundingClientRect();
            container.scrollTo({
                left: Math.max(0, (rect.width * 1.8 - container.clientWidth) / 2),
                behavior: "smooth",
            });
        }
    };
    document.addEventListener("click", toggle);
}

export default {
    extends: DefaultTheme,
    setup() {
        onMounted(enableMermaidZoom);
    },
} satisfies Theme;
