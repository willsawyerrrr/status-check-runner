from os import getenv

from .checkers import Check
from .checkers.default import DefaultChecker
from .checkers.python import PythonChecker
from .checkers.terraform import TerraformChecker
from .checkers.typescript import TypeScriptChecker
from .config import get_config
from .reporters import Reporter
from .reporters.console import ConsoleReporter
from .reporters.github_actions import GitHubActionsReporter


def resolve_checks() -> list[Check]:
    config = get_config()

    checks: list[Check] = DefaultChecker.get_checks(config)

    if config.python:
        checks.extend(PythonChecker.get_checks(config.python))
    if config.terraform:
        checks.extend(TerraformChecker.get_checks(config.terraform))
    if config.typescript:
        checks.extend(TypeScriptChecker.get_checks(config.typescript))

    return checks


def resolve_reporter() -> Reporter:
    if getenv("GITHUB_ACTIONS"):
        return GitHubActionsReporter()

    return ConsoleReporter()
