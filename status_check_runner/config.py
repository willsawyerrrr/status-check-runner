import json
from typing import Optional

import tomllib

from .checkers.default import DefaultChecker
from .checkers.python import PythonChecker
from .checkers.terraform import TerraformChecker
from .checkers.typescript import TypeScriptChecker


class Config(DefaultChecker.Config):
    python: Optional[PythonChecker.Config] = None
    terraform: Optional[TerraformChecker.Config] = None
    typescript: Optional[TypeScriptChecker.Config] = None


def get_config() -> Config:
    with open("pyproject.toml", "rb") as file:
        pyproject_toml = tomllib.load(file)

    return Config.model_validate(pyproject_toml.get("tool", {}).get("status-check-runner", {}))


def update_config_json_schema():
    with open("config-schema.json", "w", encoding="utf-8") as file:
        json.dump(Config.model_json_schema(), file, indent=4)
