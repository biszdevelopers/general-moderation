# Contributing

Thank you for contributing to the moderation service. This repository
follows strict engineering conventions; please read this guide before
opening a pull request.

## Commit Rules

**One file per commit.** Every commit touches exactly one file. This keeps
history reviewable and bisectable.

### Commit Message Format

```
[COMPONENT] Brief description of the change

- Detailed explanation
- Use American English spelling
```

### Component Tags

| Tag | Component |
| :--- | :--- |
| `[MODEL]` | Python dataclasses, enums |
| `[DETECTOR]` | Any Python detector class |
| `[AI]` | LlamaCppDetector |
| `[ENGINE]` | ModerationEngine |
| `[ADMIN]` | Python admin endpoints |
| `[UTILS]` | Python helpers |
| `[CONFIG]` | config.py, .env.example |
| `[MAIN]` | main.py, run.py |
| `[DEPLOY]` | gunicorn.conf.py, systemd, FRP |
| `[SECURITY]` | Security middleware, auth |
| `[UI]` | TypeScript/React components |
| `[UI-COMPONENT]` | Reusable UI component |
| `[UI-STYLES]` | CSS files |
| `[UI-TYPES]` | TypeScript type definitions |
| `[WORDBANK]` | WordBankManager, storage |
| `[DOCS]` | VitePress pages |
| `[TESTS]` | Test files |
| `[SCRIPTS]` | Build, test scripts |
| `[MONOREPO]` | Root-level configuration |

## Code Standards

### Python

- Java-flavored Python: classes, ABCs, dataclasses, private fields, full
  type annotations.
- No top-level functions; everything lives in a class.
- Javadoc-style docstrings with `:param`, `:return`, `:raises`.
- Format with `ruff` (4-space indent) and lint with `ruff`.
- American English everywhere.

### TypeScript / React

- Full TypeScript; no `any`.
- `*.tsx` files contain UI logic only; business logic lives in `*.ts`
  service classes.
- Functional components with hooks; Ant Design for components.
- Pure CSS with BEM naming.
- Format with `oxfmt` (4-space indent) and lint with `oxlint`.

## Verification

Before submitting:

```bash
# Backend
cd backend
ruff check app
ruff format --check app

# Frontend
cd frontend
npm run lint
npm run format:check
npm run build
```

## Testing

No local sensitive-word text files are committed. Tests must not depend on
specific dictionary contents; use the custom word bank API to seed fixtures.

## License

By contributing you agree that your contributions are licensed under the
[MIT License](../LICENSE).
