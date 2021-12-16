import pytest

from aoc2021 import day09


@pytest.mark.parametrize(
    ("name", "expected"),
    [("sample", 15), ("full", 526)],
)
def test_day09_part1(name: str, expected: int):
    data_path = f"data/day09-{name}.txt"
    assert day09.part1(data_path) == expected


@pytest.mark.parametrize(
    ("name", "expected"),
    [("sample", 1134), ("full", 1123524)],
)
def test_day09_part2(name: str, expected: int):
    data_path = f"data/day09-{name}.txt"
    assert day09.part2(data_path) == expected
