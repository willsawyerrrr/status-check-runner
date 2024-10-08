from pathlib import Path
from typing import Optional

from pydantic import BaseModel

from . import Check, Checker


class PythonChecker(Checker):
    class Config(BaseModel):
        paths: list[Path] = []
        tests_path: Optional[Path] = None

    @staticmethod
    def get_checks(config: Config) -> list[Check]:
        checks: list[Check] = []

        paths = " ".join(map(str, config.paths))

        checks.append(Check(name="Ruff Linting", command=f"ruff check {paths}"))
        checks.append(Check(name="Ruff Formatting", command=f"ruff format --check {paths}"))
        checks.append(Check(name="MyPy Type Checking", command=f"mypy {paths}"))

        if config.tests_path:
            checks.append(Check(name="Pytest Tests", command=f"pytest {config.tests_path}"))

        return checks
