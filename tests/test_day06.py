import pytest

from aoc2021 import day06


@pytest.mark.parametrize(
    ("name", "expected"),
    [("sample", 5934), ("full", 350917)],
)
def test_day06_part1(name: str, expected: int):
    data_path = f"data/day06-{name}.txt"
    assert day06.part1(data_path) == expected


@pytest.mark.parametrize(
    ("name", "expected"),
    [("sample", 26984457539), ("full", 1592918715629)],
)
def test_day06_part2(name: str, expected: int):
    data_path = f"data/day06-{name}.txt"
    assert day06.part2(data_path) == expected
