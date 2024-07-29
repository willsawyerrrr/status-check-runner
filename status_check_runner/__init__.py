import json
from typing import Optional

from .checkers import Check
from .checkers.default import DefaultChecker
from .checkers.python import PythonChecker
from .checkers.terraform import TerraformChecker
from .checkers.typescript import TypeScriptChecker
from .execute import execute_check


class Config(DefaultChecker.Config):
    python: Optional[PythonChecker.Config] = None
    terraform: Optional[TerraformChecker.Config] = None
    typescript: Optional[TypeScriptChecker.Config] = None


def update_config_json_schema():
    with open("config-schema.json", "w", encoding="utf-8") as file:
        json.dump(Config.model_json_schema(), file, indent=4)


def main() -> int:
    with open("status-checks.json", "r", encoding="utf-8") as file:
        config = Config.model_validate(json.loads(file.read()))

    checks: list[Check] = DefaultChecker.get_checks(config)

    if config.python:
        checks.extend(PythonChecker.get_checks(config.python))
    if config.terraform:
        checks.extend(TerraformChecker.get_checks(config.terraform))
    if config.typescript:
        checks.extend(TypeScriptChecker.get_checks(config.typescript))

    results: list[str] = []
    for check in checks:
        results.append(execute_check(check))

    return 0
