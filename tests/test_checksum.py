from pathlib import Path
from typing import Callable, Iterable, Tuple

from pytest import raises

from checksome import SHA256, checksum_file
from checksome.exceptions import UnexpectedEndOfBuffer


def test_has_checksum(
    data: Path,
    load_checksums: Callable[[str], Iterable[Tuple[int, int, bytes]]],
) -> None:
    with checksum_file(data / "lorum.txt", SHA256()) as cf:
        for expect in load_checksums("lorum-sha256-chunks.csv"):
            assert cf.has_checksum(
                expect[2],
                offset=expect[0],
                length=expect[1],
            )


def test_has_checksum__entire_file(data: Path) -> None:
    expect = "2943c9308a035a22207a9c204e24cfc1b8153d4502df4666a1c1b7880f3a33dd"
    with checksum_file(data / "lorum.txt", SHA256()) as cf:
        assert cf.has_checksum(expect)


def test_has_checksum__eof(
    data: Path,
    load_checksums: Callable[[str], Iterable[Tuple[int, int, bytes]]],
) -> None:
    with raises(UnexpectedEndOfBuffer) as ex:
        with checksum_file(data / "lorum.txt", SHA256()) as cf:
            for expect in load_checksums("lorum-sha256-chunks-eof.csv"):
                cf.has_checksum(
                    expect[2],
                    offset=expect[0],
                    length=expect[1],
                )

    assert str(ex.value) == "Buffer does not have 514 bytes after offset 1543"


def test_has_checksum__mismatch(
    data: Path,
    load_checksums: Callable[[str], Iterable[Tuple[int, int, bytes]]],
) -> None:
    checksums = load_checksums("lorum-sha256-chunks-mismatch.csv")
    with checksum_file(data / "lorum.txt", SHA256()) as cf:
        for index, expect in enumerate(checksums):
            has = cf.has_checksum(
                expect[2],
                offset=expect[0],
                length=expect[1],
            )
            assert has if index < 3 else not has
