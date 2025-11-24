# Task Completion Checklist
- Run available checks: currently none; if you add tests or linters, execute them via `uv run <tool>`.
- Smoke run: `uv run python main.py` to ensure the entry still works; import `root_agent` modules if touched.
- Verify dependencies untouched unless intentionally changed (pyproject.toml, uv.lock).
- Update docs if behavior or structure changes (e.g., AGENTS.md/README once populated).
- Ensure Python 3.12 compatibility and avoid introducing non-ASCII unless needed.