import json
from pathlib import Path

from pydantic import BaseModel

from .checkers import Check
from .devcontainer import execute_check, start_devcontainer


class Config(BaseModel):
    root_path: Path


def main() -> int:
    with open("config.json", "r", encoding="utf-8") as file:
        config = Config.model_validate(json.loads(file.read()))

    checks: list[Check] = []

    devcontainer_id = start_devcontainer()

    results: list[str] = []
    for check in checks:
        results.append(execute_check(devcontainer_id, check))

    return 0
