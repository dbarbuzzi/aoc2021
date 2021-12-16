from typing import List, Tuple

DATA_PATH = "data/day09-full.txt"


def load_lines(fp: str) -> List[List[int]]:
    with open(fp) as f:
        return [list(map(int, line.strip())) for line in f if line.strip()]


def is_low_point(num: int, x: int, y: int, grid: List[List[int]]) -> bool:
    # TODO: see if commented solution should be salvaged or stripped
    adjacents = set()
    if y > 0:
        adjacents.add(grid[y - 1][x])
    if y < len(grid) - 1:
        adjacents.add(grid[y + 1][x])
    if x > 0:
        adjacents.add(grid[y][x - 1])
    if x < len(grid[y]) - 1:
        adjacents.add(grid[y][x + 1])

    return num < min(adjacents)

    # if num < min(adjacents):
    #     print(num, adjacents)
    #     return True

    # return False

    # if y > 0 and grid[y - 1][x] <= num:
    #     return False
    # if y < len(grid) - 1 and grid[y + 1][x] <= num:
    #     return False
    # if x > 0 and grid[y][x - 1] <= num:
    #     return False
    # if x < len(grid[y]) - 1 and grid[y][x] + 1 <= num:
    #     return False
    # return True


def calc_basin_size(
    point: Tuple[int, int], grid: List[List[int]], visited: List[List[bool]]
) -> int:
    x, y = point
    if visited[y][x]:
        return 0
    adjacents = set()
    if y > 0 and not visited[y - 1][x]:
        adjacents.add((x, y - 1))
    if y < len(grid) - 1 and not visited[y + 1][x]:
        adjacents.add((x, y + 1))
    if x > 0 and not visited[y][x - 1]:
        adjacents.add((x - 1, y))
    if x < len(grid[y]) - 1 and not visited[y][x + 1]:
        adjacents.add((x + 1, y))

    visited[y][x] = True
    return 1 + sum(calc_basin_size(point, grid, visited) for point in adjacents)


def part1(data_path: str = DATA_PATH) -> int:
    grid = load_lines(data_path)
    total = 0
    for y, row in enumerate(grid):
        for x, num in enumerate(row):
            if num < 9 and is_low_point(num, x, y, grid):
                total += num + 1
    return total


def part2(data_path: str = DATA_PATH) -> int:
    grid = load_lines(data_path)
    visited = [[False for _ in row] for row in grid]

    # first, find all low points
    low_points: List[Tuple[int, int]] = []
    for y, row in enumerate(grid):
        for x, num in enumerate(row):
            if num == 9:
                visited[y][x] = True
            elif is_low_point(num, x, y, grid):
                point = (x, y)
                low_points.append(point)

    # next, iterate each low point and find the size of the containing basin
    sizes = [calc_basin_size(point, grid, visited) for point in low_points]

    # finally, multiply three largest basins
    a, b, c = sorted(sizes)[-3:]
    return a * b * c
