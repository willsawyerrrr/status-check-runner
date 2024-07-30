from actions_toolkit import core

from ..execute import Result
from . import Reporter


class GitHubActionsReporter(Reporter):
    def report_success(self, result: Result):
        core.debug(f"{result.check.name} succeeded!")

    def report_failure(self, result: Result):
        core.start_group(f"{result.check.name} failed ({result.status})")

        core.warning(result.stdout)

        if result.stderr:
            core.error(result.stderr)

        core.end_group()
