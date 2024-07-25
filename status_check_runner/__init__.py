import json
from pathlib import Path
from typing import Optional

from .checkers import Check
from .checkers.default import DefaultChecker
from .checkers.python import PythonChecker
from .checkers.typescript import TypeScriptChecker
from .devcontainer import execute_check, start_devcontainer


class Config(DefaultChecker.Config):
    root_path: Path
    python: Optional[PythonChecker.Config] = None
    typescript: Optional[TypeScriptChecker.Config] = None


def main() -> int:
    with open("config.json", "r", encoding="utf-8") as file:
        config = Config.model_validate(json.loads(file.read()))

    checks: list[Check] = DefaultChecker.get_checks(config.root_path, config)

    if config.python:
        checks.extend(PythonChecker.get_checks(config.root_path, config.python))
    if config.typescript:
        checks.extend(TypeScriptChecker.get_checks(config.root_path, config.typescript))

    devcontainer_id = start_devcontainer()

    results: list[str] = []
    for check in checks:
        results.append(execute_check(devcontainer_id, check))

    return 0
