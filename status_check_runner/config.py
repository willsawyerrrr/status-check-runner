import json
from typing import Any, Optional

import jsonref  # type: ignore
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
    json_schema = Config.model_json_schema()
    json_schema: dict[str, Any] = jsonref.replace_refs(json_schema)  # type: ignore

    # Shallow copy so that we can remove `$defs` from the schema which is to be dumped.
    # The original copy still has `$defs` and hence references can be resolved.
    new_json_schema = json_schema.copy()
    new_json_schema.pop("$defs")

    with open("config-schema.json", "w", encoding="utf-8") as file:
        json.dump(new_json_schema, file, indent=4)
