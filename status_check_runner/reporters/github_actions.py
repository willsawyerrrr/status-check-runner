import github_action_utils as gha_utils

from ..execute import Result
from . import Reporter


class GitHubActionsReporter(Reporter):
    def report_success(self, result: Result):
        gha_utils.debug(f"{result.check.name} succeeded!")

    def report_failure(self, result: Result):
        with gha_utils.group(f"{result.check.name} failed ({result.status})"):
            gha_utils.warning(result.stdout)

            if result.stderr:
                gha_utils.error(result.stderr)
