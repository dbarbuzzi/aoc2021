from aoc2021 import day02


def test_day02_part1():
    data_path = "data/day02-sample.txt"
    assert day02.part1(data_path) == 150


def test_day02_part2():
    data_path = "data/day02-sample.txt"
    assert day02.part2(data_path) == 900
