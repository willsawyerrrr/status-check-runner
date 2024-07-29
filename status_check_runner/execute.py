import subprocess
import sys

from .checkers import Check


def execute_check(check: Check) -> str:
    try:
        output = subprocess.check_output(
            f"{check.command}".split(), stderr=subprocess.STDOUT, text=True
        )
        print(f"{check.name} succeeded!")
        return output
    except subprocess.CalledProcessError as exc:
        print(f"{check.name} failed with exit code {exc.returncode}", file=sys.stderr)
        print(exc.output, file=sys.stderr)
        return exc.output
