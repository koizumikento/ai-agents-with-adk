# Repository Guidelines

## Project Structure & Module Organization
- `main.py`: minimal entry that prints a greeting; useful as a smoke check.
- `todo_generator/agent.py`: defines the pydantic `Todo` model and `root_agent`; update prompts or tools here.
- `todo_generator/.env`: place API keys or provider settings locally; keep secrets out of git.
- `pyproject.toml` and `uv.lock`: Python 3.12 toolchain and locked dependencies via `uv`.
- `.python-version`: pins the interpreter for contributors.

## Build, Test, and Development Commands
- `uv sync`: install or refresh the locked environment (creates `.venv`).
- `uv run python main.py`: run the hello-world entry and verify the env is sane.
- `uv run python -i todo_generator/agent.py`: load `root_agent` for interactive calls.
- `uv run python`: open a REPL with project deps available.
- `uv run pytest`: preferred test runner once tests are added.

## Coding Style & Naming Conventions
- Follow PEP 8 with 4-space indents; prefer type hints for public functions.
- Imports grouped stdlib -> third-party -> local; keep existing single-quote style.
- Names: PascalCase for models/classes (`Todo`), snake_case for functions/vars, agents stay `root_agent` unless multiple are present.
- Keep functions small and side-effect aware; add brief docstrings only when behavior is non-obvious.

## Testing Guidelines
- Framework: pytest (not yet present). Place suites under `tests/` with files named `test_*.py`.
- Mock external calls and LLM clients; avoid network-required tests. Include fast smoke coverage for `main.py` output and agent configuration.
- Run `uv run pytest` before publishing changes; aim to cover new logic you introduce.

## Commit & Pull Request Guidelines
- No commit history yet; use Conventional Commits (`feat:`, `fix:`, `chore:`, `docs:`) to keep history readable.
- PRs should explain what/why, list manual checks (e.g., `uv run python main.py`, `uv run pytest`), and link issues when relevant.
- Include screenshots or sample output when it clarifies behavior changes.

## Security & Configuration Tips
- Keep secrets in env vars or `todo_generator/.env`; never commit them.
- Regenerate the lockfile with `uv lock` only when dependencies change; follow with `uv sync` to refresh the environment.
