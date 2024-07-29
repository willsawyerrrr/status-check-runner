import json
from typing import Optional

from . import devcontainer
from .checkers import Check
from .checkers.default import DefaultChecker
from .checkers.python import PythonChecker
from .checkers.terraform import TerraformChecker
from .checkers.typescript import TypeScriptChecker


class Config(DefaultChecker.Config):
    python: Optional[PythonChecker.Config] = None
    terraform: Optional[TerraformChecker.Config] = None
    typescript: Optional[TypeScriptChecker.Config] = None


def update_config_json_schema():
    with open("config-schema.json", "w", encoding="utf-8") as file:
        json.dump(Config.model_json_schema(), file, indent=4)


def main() -> int:
    with open("config.json", "r", encoding="utf-8") as file:
        config = Config.model_validate(json.loads(file.read()))

    devcontainer_id = devcontainer.start()
    root_path = devcontainer.get_root_path(devcontainer_id)

    checks: list[Check] = DefaultChecker.get_checks(root_path, config)

    if config.python:
        checks.extend(PythonChecker.get_checks(root_path, config.python))
    if config.terraform:
        checks.extend(TerraformChecker.get_checks(root_path, config.terraform))
    if config.typescript:
        checks.extend(TypeScriptChecker.get_checks(root_path, config.typescript))

    results: list[str] = []
    for check in checks:
        results.append(devcontainer.execute_check(devcontainer_id, check))

    return 0
