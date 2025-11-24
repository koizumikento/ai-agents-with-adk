# Repository Guidelines

## Project Structure & Module Organization
- `main.py` prints "Hello from ai-agents!" for a quick sanity check.
- Agents: `finance_agent/` (coordinator plus `jp_agent.py`, `us_agent.py`, `tools.py`), `game_finder/agent.py`, and `todo_generator/agent.py` with `Todo`/`TodoPlan` schemas. Each folder keeps its own `.env` for per-agent secrets; leave them untracked.
- Tooling: `pyproject.toml` + `uv.lock` (Python 3.12, google-adk; dev `ruff`/`pytest`), `.python-version`, `.gitignore`, and lint cache `.ruff_cache/`.

## Build, Test, and Development Commands
- `uv sync` - install dependencies into `.venv` from `pyproject.toml`/`uv.lock`.
- `uv run python main.py` - smoke-check the environment.
- `uv run python -i finance_agent/agent.py` (or `game_finder/agent.py`, `todo_generator/agent.py`) - load `root_agent` for quick manual runs.
- `uv run ruff check .` - lint (dev extra).
- `uv run pytest` - run tests when added; place suites under `tests/`.

## Coding Style & Naming Conventions
- Python 3.12, PEP 8, 4-space indents; prefer single quotes as in existing modules. Import order: stdlib, third-party, local.
- Classes/models PascalCase, functions/vars/fields lower_snake_case; exported agents stay named `root_agent`.
- Keep Japanese instructions and Markdown templates embedded in agents; avoid rewriting without product agreement.
- Type hints expected; docstrings only when behavior is non-obvious; keep callbacks/tools small and pure when possible.

## Testing Guidelines
- Use pytest; name files `tests/test_*.py` and functions `test_*`.
- Mock networked `google_search`/tool calls; unit-test helpers like `append_current_time_instruction` and schema validation for `Todo`/`TodoPlan`.
- Add regression tests when adjusting prompt templates or time-handling logic; run `uv run pytest` before PRs.

## Commit & Pull Request Guidelines
- Use concise, imperative titles similar to history (e.g., `Add game_finder agent`, `Refactor agents and update documentation`); include scope in one line.
- Squash small WIP commits locally; keep body limited to rationale/notes if needed.
- PRs should describe purpose, key changes, and manual check steps (agents load, lint/tests run); link issues and attach screenshots or sample agent outputs when applicable.

## Security & Configuration Tips
- Keep API keys and search credentials in per-agent `.env` files; never commit them. `.gitignore` already covers `.env` and `.venv`.
- When adding tools, avoid logging user prompts or secrets; prefer configuration via environment variables.
