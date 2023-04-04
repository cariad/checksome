from io import StringIO
from pathlib import Path

from checksome import SHA256
from checksome.cli.args import TaskArgs
from checksome.cli.checksome_task import ChecksomeTask


def test_invoke(data: Path) -> None:
    args = TaskArgs(
        algorithm=SHA256,
        source=data / "lorum.txt",
    )

    out = StringIO()
    assert ChecksomeTask(args, out).invoke() == 0

    expect = "2943c9308a035a22207a9c204e24cfc1b8153d4502df4666a1c1b7880f3a33dd\n"
    assert out.getvalue() == expect
