from abc import abstractmethod
from typing import Iterable

from ..execute import Result


class Reporter:
    @abstractmethod
    def report_success(self, result: Result):
        """
        Report the given success of a check.

        Parameters
        ----------
            `result` (`result`): The success.
        """

    @abstractmethod
    def report_failure(self, result: Result):
        """
        Report the given failure of a check.

        Parameters
        ----------
            `result` (`Result`): The failure.
        """

    def report_all(self, results: Iterable[Result]):
        """
        Report the given results of checks.

        Parameters
        ----------
            `results` (`Iterable[Result]`): The results to report.
        """

        for result in results:
            if result.status:
                self.report_failure(result)
            else:
                self.report_success(result)
