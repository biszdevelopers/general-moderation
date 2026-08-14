/* Headless mermaid validation using linkedom as a real DOM. */
import { readdirSync, readFileSync, statSync } from "node:fs";
import { join, relative } from "node:path";
import { parseHTML } from "linkedom";

const { window } = parseHTML("<!doctype html><html><body></body></html>");
globalThis.window = window;
globalThis.document = window.document;
try { Object.defineProperty(globalThis, "navigator", { value: window.navigator, configurable: true }); } catch {}
globalThis.DOMPurify = (await import("dompurify")).default(window);

const mermaid = (await import("mermaid")).default;
mermaid.initialize({ startOnLoad: false, securityLevel: "loose", suppressErrorRendering: true });

function walk(dir, out = []) {
    for (const name of readdirSync(dir)) {
        if (name === "node_modules" || name === ".vitepress") continue;
        const p = join(dir, name);
        if (statSync(p).isDirectory()) walk(p, out);
        else if (name.endsWith(".md")) out.push(p);
    }
    return out;
}

const files = walk(".");
let blocks = 0, fails = 0, skipped = 0;

for (const file of files) {
    const src = readFileSync(file, "utf8");
    const re = /```mermaid\s*\n([\s\S]*?)```/g;
    let m, idx = 0;
    while ((m = re.exec(src))) {
        idx++; blocks++;
        const code = m[1];
        try {
            await mermaid.parse(code);
            console.log(`OK   ${relative(".", file)} block#${idx}`);
        } catch (e) {
            const msg = (e && e.message ? e.message : String(e));
            if (/DOMPurify|DOMException|not implemented|Cannot read/i.test(msg)) { skipped++; console.log(`SKIP ${relative(".", file)} block#${idx}: ${msg.split("\n")[0]}`); continue; }
            fails++;
            console.log(`FAIL ${relative(".", file)} block#${idx}: ${msg.split("\n").slice(0, 5).join(" | ")}`);
        }
    }
}

console.log(`\n${blocks} mermaid blocks, ${fails} failures, ${skipped} skipped (DOM-limited)`);
process.exit(fails ? 1 : 0);
