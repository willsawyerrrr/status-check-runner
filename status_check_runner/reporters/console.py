import sys

from ..execute import Result
from . import Reporter


class ConsoleReporter(Reporter):
    def report_success(self, result: Result):
        print(f"{result.check.name} succeeded!")

    def report_failure(self, result: Result):
        print("\n" + f"{result.check.name} failed ({result.status}):")
        print("\t" + result.stdout.replace("\n", "\n\t"))

        if result.stderr:
            print("\t" + result.stderr.replace("\n", "\n\t"), file=sys.stderr)
