import subprocess
from typing import Optional

from pydantic import BaseModel

from .checkers import Check


class Result(BaseModel):
    check: Check
    status: int
    stdout: str
    stderr: Optional[str] = None


def execute_check(check: Check) -> Result:
    try:
        output = subprocess.check_output(check.command.split(), stderr=subprocess.STDOUT, text=True)
        return Result(check=check, status=0, stdout=output)
    except subprocess.CalledProcessError as exc:
        return Result(check=check, status=exc.returncode, stdout=exc.stdout, stderr=exc.stderr)
