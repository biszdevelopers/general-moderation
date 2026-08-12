// Cross-platform developer launcher for the general-moderation monorepo.
//
// Prefers uv (the modern Python toolchain) for backend commands and falls
// back to the backend virtualenv interpreter when uv is not installed.
import { spawnSync } from "node:child_process";
import { createInterface } from "node:readline/promises";
import { randomInt, randomBytes } from "node:crypto";
import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import { fileURLToPath } from "node:url";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const isWindows = process.platform === "win32";

function venvPython() {
    return isWindows
        ? path.join(root, "backend", ".venv", "Scripts", "python.exe")
        : path.join(root, "backend", ".venv", "bin", "python");
}

function uvCommand() {
    const candidates = [process.env.UV, "uv"];
    if (isWindows) {
        candidates.push(path.join(os.homedir(), ".local", "bin", "uv.exe"));
    } else {
        candidates.push(path.join(os.homedir(), ".local", "bin", "uv"));
    }
    for (const candidate of candidates) {
        if (!candidate) {
            continue;
        }
        const probe = spawnSync(candidate, ["--version"], { stdio: "ignore" });
        if (probe.status === 0) {
            return candidate;
        }
    }
    return null;
}

function npmCommand() {
    return isWindows ? "npm.cmd" : "npm";
}

function run(command, args, cwd) {
    // On Windows, .cmd shims such as npm.cmd cannot be spawned directly and
    // require a shell. Build a quoted command string to avoid the shell-args
    // deprecation warning.
    const result = isWindows && command.endsWith(".cmd")
        ? spawnSync(`${command} ${args.map((arg) => `"${arg}"`).join(" ")}`, {
              cwd,
              stdio: "inherit",
              shell: true,
          })
        : spawnSync(command, args, { cwd, stdio: "inherit" });
    if (result.status !== 0) {
        process.exit(result.status ?? 1);
    }
}

const backendDir = () => path.join(root, "backend");
const frontendDir = () => path.join(root, "frontend");

function runInBackend(toolArgs) {
    const uv = uvCommand();
    const args = Array.isArray(toolArgs) ? toolArgs : [toolArgs];
    if (uv) {
        run(uv, ["run", ...args], backendDir());
        return;
    }
    if (args[0] === "python") {
        run(venvPython(), args.slice(1), backendDir());
        return;
    }
    run(venvPython(), ["-m", ...args], backendDir());
}

function syncBackend() {
    const uv = uvCommand();
    if (uv) {
        run(uv, ["sync"], backendDir());
        return;
    }
    console.error(
        "uv is required for backend installs. Install it from https://astral.sh/uv/",
    );
    process.exit(1);
}

const SECRET_CHARSET =
    "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()-_=+";

function secureSecret(length = 48) {
    const bytes = randomBytes(length);
    let secret = "";
    for (let index = 0; index < length; index += 1) {
        secret += SECRET_CHARSET[bytes[index] % SECRET_CHARSET.length];
    }
    return secret;
}

function envPath() {
    return path.join(backendDir(), ".env");
}

function loadEnvFile() {
    const env = envPath();
    if (!fs.existsSync(env)) {
        const example = path.join(backendDir(), ".env.example");
        if (fs.existsSync(example)) {
            fs.copyFileSync(example, env);
        } else {
            fs.writeFileSync(env, "");
        }
    }
    return fs.readFileSync(env, "utf-8");
}

function isPlaceholder(value) {
    return value.trim() === "" || value.trim().startsWith("CHANGE_ME");
}

function mask(value) {
    if (value.length <= 8) {
        return "*".repeat(value.length);
    }
    return `${value.slice(0, 2)}${"*".repeat(value.length - 4)}${value.slice(-2)}`;
}

async function genSecrets() {
    const raw = loadEnvFile();
    const lines = raw.split(/\r?\n/);
    const targets = [];
    for (const line of lines) {
        const match = line.match(/^([A-Za-z0-9_]+(?:KEY|SECRET)[A-Za-z0-9_]*)=(.*)$/);
        if (match === null) {
            continue;
        }
        const key = match[1];
        const value = match[2] ?? "";
        if (isPlaceholder(value)) {
            targets.push({ key, value });
        }
    }
    if (targets.length === 0) {
        console.log("All *_KEY and *_SECRET values in backend/.env are already set.");
        return;
    }
    const existing = lines.some(
        (line) =>
            /^([A-Za-z0-9_]+(?:KEY|SECRET)[A-Za-z0-9_]*)=/.test(line) &&
            !isPlaceholder(line.split("=", 2)[1] ?? ""),
    );
    if (existing && process.stdin.isTTY) {
        const rl = createInterface({ input: process.stdin, output: process.stdout });
        const answer = await rl.question(
            "backend/.env already contains real secrets. Regenerate placeholders? (y/N) ",
        );
        rl.close();
        if (answer.trim().toLowerCase() !== "y") {
            console.log("Aborted: no secrets were changed.");
            return;
        }
    }
    const generated = new Map();
    const next = lines.map((line) => {
        for (const { key } of targets) {
            if (!line.startsWith(`${key}=`)) {
                continue;
            }
            const value = secureSecret();
            generated.set(key, value);
            return `${key}=${value}`;
        }
        return line;
    });
    for (const { key } of targets) {
        if (!generated.has(key)) {
            const value = secureSecret();
            generated.set(key, value);
            next.push(`${key}=${value}`);
        }
    }
    fs.writeFileSync(envPath(), `${next.join("\n").replace(/\n+$/, "")}\n`);
    console.log(`Generated ${generated.size} secret(s) in backend/.env:`);
    for (const [key, value] of generated) {
        console.log(`  ${key}=${mask(value)}`);
    }
    console.log("Full values are written to backend/.env only.");
}

const command = process.argv[2];
switch (command) {
    case "backend":
        runInBackend([
            "python",
            "-m",
            "uvicorn",
            "app.main:app",
            "--host",
            "127.0.0.1",
            "--port",
            "8080",
        ]);
        break;
    case "backend-prod":
        // Gunicorn requires fcntl and is Unix-only; on Windows the single
        // Uvicorn worker from run.py reads the same .env configuration. The
        // venv interpreter is used directly so uv never re-syncs the
        // manually-installed llama-cpp-python wheel.
        if (isWindows) {
            run(venvPython(), ["run.py"], backendDir());
        } else {
            runInBackend(["gunicorn", "-c", "gunicorn.conf.py", "app.main:app"]);
        }
        break;
    case "download":
        runInBackend(["python", "-m", "app.ai.download"]);
        break;
    case "gen-secrets":
        genSecrets();
        break;
    case "install":
        run(npmCommand(), ["install"], root);
        syncBackend();
        run(npmCommand(), ["install"], frontendDir());
        break;
    case "install-backend":
        syncBackend();
        break;
    case "format-backend":
        runInBackend(["ruff", "format", "app", "run.py", "gunicorn.conf.py"]);
        break;
    case "lint-backend":
        runInBackend(["ruff", "check", "app", "run.py", "gunicorn.conf.py"]);
        break;
    case "format":
        runInBackend(["ruff", "format", "app", "run.py", "gunicorn.conf.py"]);
        run(npmCommand(), ["run", "format"], frontendDir());
        break;
    case "lint":
        runInBackend(["ruff", "check", "app", "run.py", "gunicorn.conf.py"]);
        run(npmCommand(), ["run", "lint"], frontendDir());
        break;
    default:
        console.error(`Unknown dev command: ${command}`);
        process.exit(1);
}
