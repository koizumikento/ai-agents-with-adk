# Project Overview
- Purpose: Simple Python 3.12 workspace showcasing Google ADK agents. Contains a hello-world entry point and two agent definitions (general-purpose and TODO data model helper).
- Stack: Python 3.12, google-adk, pydantic (via Google ADK dependency tree), managed with uv (pyproject/uv.lock).
- Layout:
  - `main.py`: prints "Hello from ai-agents!".
  - `task-agent/agent.py`: defines a generic LLM Agent named `root_agent` using google.adk.agents.llm_agent.Agent.
  - `todo_generator/agent.py`: defines a pydantic `Todo` model and a `root_agent` configured similarly.
  - Tooling files: `.python-version` (3.12), `.gitignore`, `pyproject.toml`, `uv.lock`.
- No tests, docs, or configuration files beyond the above; README is empty.