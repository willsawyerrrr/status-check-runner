from pydantic import BaseModel

from . import Check, Checker


class TerraformChecker(Checker):
    class Config(BaseModel):
        pass

    @staticmethod
    def get_checks(config: Config) -> list[Check]:
        checks: list[Check] = []

        checks.append(Check(name="Terraform Formatting", command="terraform fmt -check ."))

        return checks
