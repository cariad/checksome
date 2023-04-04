from typing import Type

from pytest import mark, raises

from checksome import SHA256, Algorithm
from checksome.algorithms import get_algorithm


@mark.parametrize(
    "name, expect",
    [
        ("sha256", SHA256),
        ("SHA256", SHA256),
    ],
)
def test_get_algorithm(name: str, expect: Type[Algorithm]) -> None:
    assert get_algorithm(name) is expect


def test_get_algorithm__not_found() -> None:
    with raises(ValueError) as ex:
        get_algorithm("foo")

    assert str(ex.value) == 'No algorithm named "foo"'
