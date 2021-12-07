from collections import Counter, defaultdict
from typing import List, Tuple

DATA_PATH = "data/day05-full.txt"


def parse_line(line: str) -> Tuple[List[int]]:
    a, b = line.split(" -> ")
    return (map(int, a.split(",")), map(int, b.split(",")))


def part1(data_path: str = DATA_PATH) -> int:
    with open(data_path) as f:
        lines = [line.strip() for line in f if line.strip()]

    grid = defaultdict(lambda: defaultdict(int))
    for line in lines:
        ([ax, ay], [bx, by]) = parse_line(line)
        if ax == bx:
            top, bottom = max(ay, by), min(ay, by)
            i = top
            while i >= bottom:
                grid[ax][i] += 1
                i -= 1
        elif ay == by:
            left, right = min(ax, bx), max(ax, bx)
            i = left
            while i <= right:
                grid[i][ay] += 1
                i += 1

    counter = Counter()
    for row in grid.values():
        counter.update(row.values())

    return sum(v for k, v in counter.items() if k > 1)


def part2(data_path: str = DATA_PATH):
    with open(data_path) as f:
        lines = [line.strip() for line in f if line.strip()]

    grid = defaultdict(lambda: defaultdict(int))
    for line in lines:
        ([ax, ay], [bx, by]) = parse_line(line)
        if ax == bx:
            top, bottom = max(ay, by), min(ay, by)
            i = top
            while i >= bottom:
                grid[ax][i] += 1
                i -= 1
        elif ay == by:
            left, right = min(ax, bx), max(ax, bx)
            i = left
            while i <= right:
                grid[i][ay] += 1
                i += 1
        else:
            dx = 1 if bx > ax else -1
            dy = 1 if by > ay else -1
            x, y = ax, ay
            for _ in range(abs(ax - bx) + 1):
                grid[x][y] += 1
                x += dx
                y += dy

    counter = Counter()
    for row in grid.values():
        counter.update(row.values())

    return sum(v for k, v in counter.items() if k > 1)
