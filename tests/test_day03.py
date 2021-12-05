from aoc2021 import day03


def test_day03_part1():
    data_path = "data/day03-sample.txt"
    assert day03.part1(data_path) == 198


def test_day03_part2():
    data_path = "data/day03-sample.txt"
    assert day03.part2(data_path) == 23 * 10  # O2 generator = 23; CO2 scrubber = 10
