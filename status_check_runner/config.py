import json
from typing import Optional

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
