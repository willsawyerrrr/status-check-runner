from pathlib import Path

from pydantic import BaseModel

from . import Check, Checker


class TypeScriptChecker(Checker):
    class Config(BaseModel):
        paths: list[Path] = []

    @staticmethod
    def get_checks(root_path: Path, config: Config) -> list[Check]:
        checks: list[Check] = []

        for path in config.paths:
            checks.append(
                Check(
                    name=f"TypeScript Compiler ({path})",
                    command=f"npx tsc --noEmit --project {root_path / path}",
                )
            )

        return checks
