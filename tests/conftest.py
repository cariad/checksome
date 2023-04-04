from pathlib import Path

from pytest import fixture

from checksome.logging import logger

logger.setLevel("DEBUG")


@fixture
def lorum() -> Path:
    return Path(__file__).parent / "data" / "lorum.txt"
