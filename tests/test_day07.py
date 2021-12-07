import pytest

from aoc2021 import day07


@pytest.mark.parametrize(
    ("name", "expected"),
    [("sample", 37), ("full", 349812)],
)
def test_day07_part1(name: str, expected: int):
    data_path = f"data/day07-{name}.txt"
    assert day07.part1(data_path) == expected


@pytest.mark.parametrize(
    ("name", "expected"),
    [("sample", 168), ("full", 99763899)],
)
def test_day07_part2(name: str, expected: int):
    data_path = f"data/day07-{name}.txt"
    assert day07.part2(data_path) == expected
