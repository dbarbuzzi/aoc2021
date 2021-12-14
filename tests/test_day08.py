import pytest

from aoc2021 import day08


@pytest.mark.parametrize(
    ("name", "expected"),
    [("sample", 26), ("full", 504)],
)
def test_day08_part1(name: str, expected: int):
    data_path = f"data/day08-{name}.txt"
    assert day08.part1(data_path) == expected


@pytest.mark.parametrize(
    ("name", "expected"),
    [("sample", 61229), ("full", 1073431)],
)
def test_day08_part2(name: str, expected: int):
    data_path = f"data/day08-{name}.txt"
    assert day08.part2(data_path) == expected
