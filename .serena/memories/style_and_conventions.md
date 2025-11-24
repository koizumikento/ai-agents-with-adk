# Style and Conventions
- Language: Python 3.12. Follow standard PEP 8 formatting and typing (type hints already used on pydantic model).
- Lint/format: No configured tools (no Black/Ruff/isort configs). Use common defaults if adding (e.g., Black, Ruff) but keep consistent.
- Imports: Standard library first, third-party next. Existing files use single quotes and simple assignment style.
- Naming: Agents named `root_agent`; pydantic model `Todo` with lower_snake_case fields. Prefer PascalCase for models/classes, lower_snake_case for functions/variables.
- Docstrings/comments: None present; add concise docstrings only when behavior is non-trivial.