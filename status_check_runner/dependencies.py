import json

from .checkers import Check
from .checkers.default import DefaultChecker
from .checkers.python import PythonChecker
from .checkers.terraform import TerraformChecker
from .checkers.typescript import TypeScriptChecker
from .config import Config
from .reporters import Reporter
from .reporters.console import ConsoleReporter


def resolve_checks() -> list[Check]:
    with open("status-checks.json", "r", encoding="utf-8") as file:
        config = Config.model_validate(json.loads(file.read()))

    checks: list[Check] = DefaultChecker.get_checks(config)

    if config.python:
        checks.extend(PythonChecker.get_checks(config.python))
    if config.terraform:
        checks.extend(TerraformChecker.get_checks(config.terraform))
    if config.typescript:
        checks.extend(TypeScriptChecker.get_checks(config.typescript))

    return checks


def resolve_reporter() -> Reporter:
    return ConsoleReporter()
