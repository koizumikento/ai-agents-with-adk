# Repository Guidelines

## Project Structure & Modules

- `main.py` is a simple greeting entry point for smoke-testing the environment.
- `game_finder/agent.py`: `CurrentTimeInstructionTool` (BaseTool override) injects the current timestamp into prompts; `game_finder_agent` uses `google_search`; instructions expect Japanese Markdown sections that include a '最終更新' line.
- `todo_generator/agent.py`: Pydantic models `Todo` and `TodoPlan` plus `todo_generator_agent`; the instruction mandates at least one `google_search` call and returns Japanese JSON matching the schema with citations.
- `.env` files in agent folders are reserved for secrets (API keys, etc.); keep them local and git-ignored. Tooling lives in `pyproject.toml`, `uv.lock`, and `.python-version` (Python 3.12).

## Build, Test, Development Commands

- `uv sync` - install locked dependencies into `.venv`.
- `uv run python main.py` - quick sanity check.
- `uv run python -i game_finder/agent.py` (or `todo_generator/agent.py`) - drop into a REPL with the module loaded; `game_finder_agent` / `todo_generator_agent` are ready for manual calls.
- No baked-in tests yet; if you add tooling, prefer `uv run <cmd>` (e.g., `uv run pytest`) to reuse the environment.

## Coding Style & Naming Conventions

- Follow PEP 8 with type hints; order imports stdlib -> third-party; prefer single quotes.
- Use PascalCase for classes/models and snake_case for functions/variables; exported agents keep the `_agent` suffix and uppercase `INSTRUCTION` constants.
- Keep system prompts concise and Japanese to match existing behavior; preserve markdown/JSON output templates.

## Testing Guidelines

- Add tests under `tests/` using `test_*.py`; target pytest for new suites.
- Mock `google_adk` interactions or stub networked tools; validate tool wiring (e.g., required `google_search` calls, timestamp injection) and schema outputs.

## Commit & Pull Request Guidelines

- Commit history uses short, imperative messages (e.g., "Add game_finder agent and current time instruction tool"); follow suit.
- PRs should summarize scope, list key commands run, link issues, and include sample agent inputs/outputs or screenshots. Note any env vars or secrets required to reproduce.
