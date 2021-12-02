DATA_PATH = "data/day01-full.txt"


def part1(data_path=DATA_PATH):
    with open(data_path) as f:
        lines = [line.strip() for line in f]

    return sum(int(b) > int(a) for a, b in zip(lines[:-1], lines[1:]))


def part2(data_path=DATA_PATH):
    with open(data_path) as f:
        lines = [line.strip() for line in f]

    return sum(
        sum((int(b), int(c), int(d))) > sum((int(a), int(b), int(c)))
        for a, b, c, d in zip(lines[:-3], lines[1:-2], lines[2:-1], lines[3:])
    )
