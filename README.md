# Status Check Runner

Configure this tool with the `[tool.status-check-runner]` table in your `pyproject.toml`.

```toml
# pyproject.toml

[tool.status-check-runner.python]
paths = ["src", "tests"]

# or, equivalently

[tool.status-check-runner]
python = { paths = ["src", "tests"] }
```
