from csv import reader
from pathlib import Path
from typing import Callable, Iterable, Tuple

from pytest import fixture

from checksome.logging import logger

logger.setLevel("DEBUG")


@fixture
def data() -> Path:
    return Path(__file__).parent / "data"


@fixture
def load_checksums(
    data: Path,
) -> Callable[[str], Iterable[Tuple[int, int, bytes]]]:
    def load(filename: str) -> Iterable[Tuple[int, int, bytes]]:
        with open(data / filename) as f:
            for row in reader(f):
                yield (
                    int(row[0]),
                    int(row[1]),
                    bytes.fromhex(row[2]),
                )

    return load
