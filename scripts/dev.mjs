// Cross-platform developer launcher for the moderation monorepo.
//
// Resolves the backend virtualenv interpreter and the platform npm command so
// the root package.json scripts work identically on Windows and Linux.
import { spawnSync } from "node:child_process";
import path from "node:path";
import { fileURLToPath } from "node:url";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const isWindows = process.platform === "win32";

function venvPython() {
    return isWindows
        ? path.join(root, "backend", ".venv", "Scripts", "python.exe")
        : path.join(root, "backend", ".venv", "bin", "python");
}

function npmCommand() {
    return isWindows ? "npm.cmd" : "npm";
}

function run(command, args, cwd) {
    const result = spawnSync(command, args, { cwd, stdio: "inherit" });
    if (result.status !== 0) {
        process.exit(result.status ?? 1);
    }
}

const command = process.argv[2];
switch (command) {
    case "backend":
        run(
            venvPython(),
            ["-m", "uvicorn", "app.main:app", "--host", "127.0.0.1", "--port", "8080"],
            path.join(root, "backend"),
        );
        break;
    case "install":
        run(npmCommand(), ["install"], root);
        run(
            venvPython(),
            ["-m", "pip", "install", "-r", "requirements.txt"],
            path.join(root, "backend"),
        );
        run(npmCommand(), ["install"], path.join(root, "frontend"));
        break;
    case "format":
        run(
            venvPython(),
            ["-m", "ruff", "format", "app", "run.py", "gunicorn.conf.py"],
            path.join(root, "backend"),
        );
        run(npmCommand(), ["run", "format"], path.join(root, "frontend"));
        break;
    case "lint":
        run(
            venvPython(),
            ["-m", "ruff", "check", "app", "run.py", "gunicorn.conf.py"],
            path.join(root, "backend"),
        );
        run(npmCommand(), ["run", "lint"], path.join(root, "frontend"));
        break;
    default:
        console.error(`Unknown dev command: ${command}`);
        process.exit(1);
}
