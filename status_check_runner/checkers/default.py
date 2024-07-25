from pathlib import Path

from pydantic import BaseModel

from . import Check, Checker


class DefaultChecker(Checker):
    class Config(BaseModel):
        pass

    @staticmethod
    def get_checks(root_path: Path, config: Config) -> list[Check]:
        checks: list[Check] = []

        checks.append(
            Check(
                name=f"Prettier Formatting ({root_path})",
                command=f"npx prettier --check {root_path}",
            )
        )

        return checks
