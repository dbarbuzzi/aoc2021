from aoc2021 import day04


def test_day04_part1():
    data_path = "data/day04-sample.txt"
    # sum unmarked = 188; last called = 24
    assert day04.part1(data_path) == 188 * 24


def test_day04_part2():
    data_path = "data/day04-sample.txt"
    # last bingo sum unmarked = 148; last called = 13
    assert day04.part2(data_path) == 148 * 13
