# Suggested Commands
- Install deps (uv): `uv sync` (uses pyproject.toml and uv.lock; creates .venv if absent).
- Run main entry: `uv run python main.py` (prints the hello message).
- Explore agents: `uv run python -i task-agent/agent.py` or `uv run python -i todo_generator/agent.py` to load `root_agent` objects for interactive experimentation.
- REPL with project env: `uv run python` (ensures google-adk available).
- Lint/format/tests: none configured; if added, prefer running via `uv run <tool>` to reuse environment.