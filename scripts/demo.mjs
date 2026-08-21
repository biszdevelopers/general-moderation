// One-command demo: boot the service, run the accuracy gate, pre-warm the
// model and semantic layer, then open the admin console and workbench.
//
// Usage:
//   node scripts/demo.mjs            # full demo (build if needed, eval, boot, open)
//   node scripts/demo.mjs --skip-eval
//   node scripts/demo.mjs --no-open  # do not launch a browser
//   node scripts/demo.mjs messages   # just print the curated demo messages
import { spawn, spawnSync } from "node:child_process";
import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { setTimeout as sleep } from "node:timers/promises";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const isWindows = process.platform === "win32";
const baseUrl = process.env.DEMO_BASE_URL || "http://127.0.0.1:18427";

function readEnv(key) {
    const envPath = path.join(root, "backend", ".env");
    if (!fs.existsSync(envPath)) {
        return "";
    }
    for (const line of fs.readFileSync(envPath, "utf-8").split(/\r?\n/)) {
        if (line.startsWith(`${key}=`)) {
            return line.slice(key.length + 1).trim();
        }
    }
    return "";
}

const adminKey = readEnv("ADMIN_API_KEY");
const adminHeaders = adminKey ? { "X-API-Key": adminKey } : {};

async function adminFetch(pathname) {
    const response = await fetch(`${baseUrl}${pathname}`, { headers: adminHeaders });
    if (!response.ok) {
        return {};
    }
    return response.json();
}

function venvPython() {
    return isWindows
        ? path.join(root, "backend", ".venv", "Scripts", "python.exe")
        : path.join(root, "backend", ".venv", "bin", "python");
}

function run(cmd, args, opts = {}) {
    const result = spawnSync(cmd, args, { stdio: "inherit", ...opts });
    if (result.status !== 0) {
        process.exit(result.status ?? 1);
    }
}

function runQuiet(cmd, args, opts = {}) {
    return spawnSync(cmd, args, { encoding: "utf-8", ...opts });
}

function open(url) {
    const opener = isWindows ? "cmd" : os.platform() === "darwin" ? "open" : "xdg-open";
    const args = isWindows ? ["/c", "start", "", url] : [url];
    spawn(opener, args, { stdio: "ignore", detached: true }).unref();
}

function printMessages() {
    const payload = JSON.parse(
        fs.readFileSync(path.join(root, "scripts", "demo-messages.json"), "utf-8"),
    );
    console.log("\nCurated demo messages (moderate them live in the workbench):\n");
    for (const message of payload.messages) {
        console.log(`  [${message.lang}] ${message.label.padEnd(26)} ${message.text}`);
    }
    console.log("");
}

async function waitForHealth(timeoutMs = 180_000) {
    const deadline = Date.now() + timeoutMs;
    while (Date.now() < deadline) {
        const health = runQuiet("node", [
            "-e",
            `fetch("${baseUrl}/health").then(r=>process.exit(r.ok?0:1)).catch(()=>process.exit(1))`,
        ]);
        if (health.status === 0) {
            return true;
        }
        await sleep(2000);
    }
    return false;
}

async function prewarm() {
    // Poll admin/health until the model and semantic layer report ready, then
    // send a benign message so the full path has been exercised once.
    const admin = await adminFetch("/admin/health");
    console.log(`  llama available: ${admin.llamaAvailable}`);
    for (let attempt = 0; attempt < 90; attempt += 1) {
        const health = await adminFetch("/admin/health");
        const semantic = await adminFetch("/admin/semantic");
        const ready = health.llamaAvailable && semantic.ready;
        if (ready) {
            break;
        }
        if (attempt % 10 === 0) {
            console.log(`  prewarming (llama=${health.llamaAvailable} semantic=${semantic.ready})...`);
        }
        await sleep(2000);
    }
    await fetch(`${baseUrl}/moderate`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text: "hello world", app_name: "demo" }),
    });
    console.log("  prewarm complete.");
}

async function main() {
    const args = process.argv.slice(2);
    if (args.includes("messages")) {
        printMessages();
        return;
    }
    const skipEval = args.includes("--skip-eval");
    const noOpen = args.includes("--no-open");

    console.log("=== General Moderation demo ===\n");

    if (!fs.existsSync(path.join(root, "frontend", "dist", "index.html"))) {
        console.log("Frontend not built; building once...");
        run("npm", ["run", "build"], { cwd: root });
    }

    if (!skipEval) {
        console.log("Accuracy gate (npm run eval)...");
        run("npm", ["run", "eval"], { cwd: root });
    }

    console.log("Booting the service on", baseUrl, "...");
    const server = spawn(
        isWindows ? venvPython() : "uv",
        isWindows
            ? ["run.py"]
            : ["run", "uvicorn", "app.main:app", "--host", "127.0.0.1", "--port", "18427"],
        { cwd: path.join(root, "backend"), stdio: "inherit" },
    );
    server.on("exit", (code) => {
        console.log(`Service stopped (code ${code}).`);
        process.exit(0);
    });

    console.log("Waiting for health...");
    if (!(await waitForHealth())) {
        console.error("Service did not become healthy in time.");
        server.kill();
        process.exit(1);
    }
    console.log("Service is healthy.");

    console.log("Pre-warming model and semantic layer...");
    await prewarm();

    console.log("\nDemo is live:");
    console.log(`  Admin console: ${baseUrl}/`);
    console.log(`  Test workbench: ${baseUrl}/test-workbench`);
    console.log(`  Metrics: ${baseUrl}/metrics`);
    printMessages();
    if (!noOpen) {
        open(baseUrl + "/test-workbench");
        open(baseUrl);
    }
    console.log("Press Ctrl+C to stop.\n");
    await new Promise(() => {});
}

main().catch((error) => {
    console.error(error);
    process.exit(1);
});
