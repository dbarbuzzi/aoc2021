import pytest

from aoc2021 import day05


@pytest.mark.parametrize(
    ("name", "expected"),
    [("sample", 5), ("full", 5690)],
)
def test_day05_part1(name: str, expected: int):
    data_path = f"data/day05-{name}.txt"
    assert day05.part1(data_path) == expected


@pytest.mark.parametrize(
    ("name", "expected"),
    [("sample", 12), ("full", 17741)],
)
def test_day05_part2(name: str, expected: int):
    data_path = f"data/day05-{name}.txt"
    assert day05.part2(data_path) == expected
