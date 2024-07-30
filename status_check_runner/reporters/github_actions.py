from typing import Iterable

from actions_toolkit import core

from ..execute import Result
from . import Reporter


class GitHubActionsReporter(Reporter):
    def __init__(self):
        super().__init__()

        self.failures: list[Result] = []

    def report_success(self, result: Result):
        core.debug(f"{result.check.name} succeeded!")

    def report_failure(self, result: Result):
        self.failures.append(result)

        core.start_group(f"{result.check.name} failed ({result.status})")

        core.error(result.stdout)

        if result.stderr:
            core.error(result.stderr)

        core.end_group()

    def report_all(self, results: Iterable[Result]):
        super().report_all(results)

        if self.failures:
            core.set_failed(f"{len(self.failures)} checks failed")
