from .dependencies import resolve_checks
from .execute import Result, execute_check


def main() -> int:
    checks = resolve_checks()

    results: list[Result] = []
    for check in checks:
        results.append(execute_check(check))

    return 0
