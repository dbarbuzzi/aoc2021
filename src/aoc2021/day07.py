from functools import cache
from typing import Dict, List

DATA_PATH = "data/day07-full.txt"


def load_data(fp: str) -> List[int]:
    with open(fp) as f:
        return [*map(int, f.read().strip().split(","))]


def calc_constant_costs(crabs: List[int]) -> Dict[int, int]:
    left = min(crabs)
    right = max(crabs)
    return {
        pos: sum(abs(crab - pos) for crab in crabs) for pos in range(left, right + 1)
    }


@cache
def increasing_move_cost(distance: int) -> int:
    return sum(range(distance + 1))


def calc_increasing_cost(crabs: List[int], pos: int) -> int:
    cost = 0
    for crab in crabs:
        diff = abs(crab - pos)
        if diff > 0:
            cost += increasing_move_cost(diff)
    return cost


def calc_increasing_costs(crabs: List[int]) -> Dict[int, int]:
    left = min(crabs)
    right = max(crabs)
    return {pos: calc_increasing_cost(crabs, pos) for pos in range(left, right + 1)}


def part1(data_path: str = DATA_PATH) -> int:
    crabs = load_data(data_path)
    move_costs = calc_constant_costs(crabs)
    sorted_costs = sorted(move_costs.values())
    return sorted_costs[0]


def part2(data_path: str = DATA_PATH) -> int:
    crabs = load_data(data_path)
    move_costs = calc_increasing_costs(crabs)
    sorted_costs = sorted(move_costs.values())
    return sorted_costs[0]
