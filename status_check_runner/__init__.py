from .dependencies import resolve_checks, resolve_reporter
from .execute import Result, execute_check


def main() -> int:
    checks = resolve_checks()

    results: list[Result] = []
    for check in checks:
        results.append(execute_check(check))

    reporter = resolve_reporter()
    reporter.report_all(results)

    return 0
