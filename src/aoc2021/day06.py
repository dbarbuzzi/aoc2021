from typing import Iterator, List

DATA_PATH = "data/day06-full.txt"


def load_data(fp: str) -> Iterator[int]:
    with open(fp) as f:
        return map(int, f.read().strip().split(","))


def process_days(fish_on_day: List[int], num_days: int) -> List[int]:
    for _ in range(num_days):
        births = fish_on_day.pop(0)
        fish_on_day[6] += births
        fish_on_day.append(births)
    return fish_on_day


def part1(data_path: str = DATA_PATH) -> int:
    initial_fish = load_data(data_path)

    fish_on_day = [0] * 9
    for fish in initial_fish:
        fish_on_day[fish] += 1

    fish_on_day = process_days(fish_on_day, 80)

    return sum(fish_on_day)


def part2(data_path: str = DATA_PATH) -> int:
    initial_fish = load_data(data_path)

    fish_on_day = [0] * 9
    for fish in initial_fish:
        fish_on_day[fish] += 1

    fish_on_day = process_days(fish_on_day, 256)

    return sum(fish_on_day)
