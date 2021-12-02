import argparse

import aoc2021

solutions = {
    1: [aoc2021.day01.part1, aoc2021.day01.part2],
    2: [aoc2021.day02.part1, aoc2021.day02.part2],
}


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "day", type=int, help="which day to solve", choices=range(1, len(solutions) + 1)
    )
    parser.add_argument("part", type=int, help="which part to solve", choices=(1, 2))
    parser.add_argument("-f", "--file", type=open, help="file containing input data")
    return parser.parse_args()


def main():
    args = parse_args()
    solution = solutions[args.day][args.part - 1]
    print(solution())
