from pathlib import Path
from typing import Callable, Iterable, Tuple

from pytest import raises

from checksome import SHA256, checksum_file
from checksome.exceptions import UnexpectedEndOfBuffer


def test_has_checksums(
    data: Path,
    load_ranges: Callable[[str], Iterable[Tuple[int, int, bytes]]],
) -> None:
    with checksum_file(data / "lorum.txt", SHA256()) as cf:
        for expect in load_ranges("lorum-sha256-chunks.csv"):
            assert cf.has_checksum(expect[0], expect[1], expect[2])


def test_has_checksums__eof(
    data: Path,
    load_ranges: Callable[[str], Iterable[Tuple[int, int, bytes]]],
) -> None:
    with raises(UnexpectedEndOfBuffer) as ex:
        with checksum_file(data / "lorum.txt", SHA256()) as cf:
            for expect in load_ranges("lorum-sha256-chunks-eof.csv"):
                cf.has_checksum(expect[0], expect[1], expect[2])

    assert str(ex.value) == "Buffer does not have 514 bytes after offset 1543"


def test_has_checksums__mismatch(
    data: Path,
    load_ranges: Callable[[str], Iterable[Tuple[int, int, bytes]]],
) -> None:
    checksums = load_ranges("lorum-sha256-chunks-mismatch.csv")
    with checksum_file(data / "lorum.txt", SHA256()) as cf:
        for index, expect in enumerate(checksums):
            has = cf.has_checksum(expect[0], expect[1], expect[2])
            assert has if index < 3 else not has
