from typing import List, Type

from cline import AnyTask
from pytest import mark

from checksome import SHA256
from checksome.cli import ChecksomeCli
from checksome.cli.args import TaskArgs
from checksome.cli.checksome_task import ChecksomeTask


@mark.parametrize(
    "args, expect_task, expect_args",
    [
        (
            ["foo.txt", "sha256"],
            ChecksomeTask,
            TaskArgs(
                algorithm=SHA256,
                source="foo.txt",
            ),
        ),
    ],
)
def test(
    args: List[str],
    expect_task: Type[AnyTask],
    expect_args: TaskArgs,
) -> None:
    cli = ChecksomeCli(args=args)
    assert isinstance(cli.task, expect_task)
    assert cli.task.args == expect_args
