from pydantic import BaseModel

from . import Check, Checker


class DefaultChecker(Checker):
    class Config(BaseModel):
        pass

    @staticmethod
    def get_checks(config: Config) -> list[Check]:
        checks: list[Check] = []

        checks.append(Check(name="Prettier Formatting", command="npx prettier --check ."))

        return checks
