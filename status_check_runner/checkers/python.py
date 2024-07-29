from pathlib import Path
from typing import Optional

from pydantic import BaseModel

from . import Check, Checker


class PythonChecker(Checker):
    class Config(BaseModel):
        paths: list[Path] = []
        tests_path: Optional[Path] = None
        pytest_args: list[str] = []

    @staticmethod
    def get_checks(config: Config) -> list[Check]:
        checks: list[Check] = []

        for path in config.paths:
            checks.append(
                Check(
                    name=f"Ruff Linting ({path})",
                    command=f"ruff check {path}",
                )
            )
            checks.append(
                Check(
                    name=f"Ruff Formatting ({path})",
                    command=f"ruff format --check {path}",
                )
            )
            checks.append(
                Check(
                    name=f"MyPy Type Checking ({path})",
                    command=f"mypy {path}",
                )
            )

        if config.tests_path:
            checks.append(
                Check(
                    name=f"Pytest Tests ({path})",
                    command=f"pytest {" ".join(config.pytest_args)} {config.tests_path}",
                )
            )

        return checks
