DATA_PATH = "data/day06-full.txt"


def part1(data_path: str = DATA_PATH) -> int:
    with open(data_path) as f:
        initial_fish = map(int, f.read().strip().split(","))

    days = [0] * 9
    for fish in initial_fish:
        days[fish] += 1

    num_days = 80
    for _ in range(num_days):
        births = days.pop(0)
        days[6] += births
        days.append(births)

    return sum(days)


def part2(data_path: str = DATA_PATH) -> int:
    with open(data_path) as f:
        initial_fish = map(int, f.read().strip().split(","))

    days = [0] * 9
    for fish in initial_fish:
        days[fish] += 1

    num_days = 256
    for _ in range(num_days):
        births = days.pop(0)
        days[6] += births
        days.append(births)

    return sum(days)
