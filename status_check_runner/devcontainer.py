import json
import subprocess
import sys
from pathlib import Path

from .checkers import Check


def start() -> str:
    raw_output = subprocess.check_output("devcontainer up --workspace-folder .".split(), text=True)
    output = json.loads(raw_output)
    assert output["outcome"] == "success"
    return output["containerId"]


def get_root_path(devcontainer_id: str) -> Path:
    jq_command = '.[].Mounts[] | select(.Type == "bind") | .Destination'
    root_path = subprocess.check_output(
        f"docker inspect {devcontainer_id} | jq '{jq_command}'",
        shell=True,
        text=True,
    )
    return Path(root_path.strip()[1:-1])


def execute_check(devcontainer_id: str, root_path: Path, check: Check) -> str:
    try:
        output = subprocess.check_output(
            f"devcontainer exec --container-id {devcontainer_id} {check.command}".split(),
            stderr=subprocess.STDOUT,
            text=True,
        )
        print(f"{check.name} succeeded!")
        return output
    except subprocess.CalledProcessError as exc:
        print(f"{check.name} failed with exit code {exc.returncode}", file=sys.stderr)
        print(exc.output, file=sys.stderr)
        return exc.output
