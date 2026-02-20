from __future__ import annotations

import shlex
import subprocess
from pathlib import Path


def run_checked(command: list[str], cwd: Path | None = None) -> None:
    result = subprocess.run(command, cwd=cwd, check=False)
    if result.returncode != 0:
        cmd = shlex.join(command)
        msg = f"command failed ({result.returncode}): {cmd}"
        raise RuntimeError(msg)


def run_capture(command: list[str], cwd: Path | None = None) -> str:
    result = subprocess.run(
        command,
        cwd=cwd,
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        cmd = shlex.join(command)
        detail = (result.stderr or result.stdout).strip()
        msg = f"command failed ({result.returncode}): {cmd}: {detail}"
        raise RuntimeError(msg)
    return result.stdout.strip()
