from aoc2021 import day06


def test_day06_part1():
    data_path = "data/day06-sample.txt"
    assert day06.part1(data_path) == 5934


def test_day06_part2():
    data_path = "data/day06-sample.txt"
    assert day06.part2(data_path) == 26984457539
