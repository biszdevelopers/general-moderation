// Cross-platform developer launcher for the moderation monorepo.
//
// Prefers uv (the modern Python toolchain) for backend commands and falls
// back to the backend virtualenv interpreter when uv is not installed.
import { spawnSync } from "node:child_process";
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
