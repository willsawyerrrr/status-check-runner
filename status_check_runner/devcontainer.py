import json
import subprocess
import sys

from .checkers import Check


def start_devcontainer() -> str:
    devcontainer = subprocess.run(
        "devcontainer up --workspace-folder .".split(),
        capture_output=True,
        text=True,
    )
    assert devcontainer.returncode == 0, devcontainer.stderr
    assert devcontainer.stdout

    devcontainer_output = json.loads(devcontainer.stdout)
    assert devcontainer_output["outcome"] == "success"

    return devcontainer_output["containerId"]


def execute_check(devcontainer_id: str, check: Check) -> str:
    process = subprocess.run(
        f"devcontainer exec --container-id {devcontainer_id} {check.command}".split(),
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
    )

    if process.returncode == 0:
        print(f"{check.name} succeeded!")
    else:
        print(f"{check.name} failed with exit code {process.returncode}", file=sys.stderr)
        print(process.stdout, file=sys.stderr)

    return process.stdout
