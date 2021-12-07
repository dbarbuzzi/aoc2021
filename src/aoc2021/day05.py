from collections import Counter, defaultdict
from typing import Any, List, Tuple

DATA_PATH = "data/day05-full.txt"


def load_lines(fp: str) -> List[str]:
    with open(fp) as f:
        return [line.strip() for line in f if line.strip()]


def mark_horizontal_line(
    grid: defaultdict[Any, defaultdict[Any, int]], y: int, x1: int, x2: int
) -> defaultdict[Any, defaultdict[Any, int]]:
    dx = 1 if x1 < x2 else -1
    for i in range(abs(x1 - x2) + 1):
        grid[x1 + i * dx][y] += 1
    return grid


def mark_vertical_line(
    grid: defaultdict[Any, defaultdict[Any, int]], x: int, y1: int, y2: int
) -> defaultdict[Any, defaultdict[Any, int]]:
    dy = 1 if y1 < y2 else -1
    for i in range(abs(y1 - y2) + 1):
        grid[x][y1 + i * dy] += 1
    return grid


def mark_diagonal_line(
    grid: defaultdict[Any, defaultdict[Any, int]], x1: int, x2: int, y1: int, y2: int
) -> defaultdict[Any, defaultdict[Any, int]]:
    dx = 1 if x1 < x2 else -1
    dy = 1 if y1 < y2 else -1
    for i in range(abs(x1 - x2) + 1):
        grid[x1 + i * dx][y1 + i * dy] += 1

    return grid


def create_marked_grid(
    lines: List[str], include_diagonal: bool = False
) -> defaultdict[Any, defaultdict[Any, int]]:
    grid = defaultdict(lambda: defaultdict(int))
    for line in lines:
        [ax, ay], [bx, by] = parse_line(line)
        if ax == bx:
            grid = mark_vertical_line(grid, ax, ay, by)
        elif ay == by:
            grid = mark_horizontal_line(grid, ay, ax, bx)
        elif include_diagonal:
            grid = mark_diagonal_line(grid, ax, bx, ay, by)
    return grid


def parse_line(line: str) -> Tuple[List[int]]:
    a, b = line.split(" -> ")
    return (map(int, a.split(",")), map(int, b.split(",")))


def part1(data_path: str = DATA_PATH) -> int:
    lines = load_lines(data_path)

    grid = create_marked_grid(lines)

    counter = Counter()
    for row in grid.values():
        counter.update(row.values())

    return sum(v for k, v in counter.items() if k > 1)


def part2(data_path: str = DATA_PATH) -> int:
    lines = load_lines(data_path)

    grid = create_marked_grid(lines, include_diagonal=True)

    counter = Counter()
    for row in grid.values():
        counter.update(row.values())

    return sum(v for k, v in counter.items() if k > 1)
