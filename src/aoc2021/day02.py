DATA_PATH = "data/day02-full.txt"


def part1(data_path=DATA_PATH):
    with open(data_path) as f:
        lines = [line.strip() for line in f]

    pos = {"x": 0, "y": 0}
    for line in lines:
        cmd, val = line.split()
        val = int(val)
        if cmd == "forward":
            pos["x"] += val
        elif cmd == "down":
            pos["y"] += val
        elif cmd == "up":
            pos["y"] -= val
        else:
            raise ValueError("unsupported command: %s", cmd)

    return pos["x"] * pos["y"]


def part2(data_path=DATA_PATH):
    with open(data_path) as f:
        lines = [line.strip() for line in f]

    pos = {"x": 0, "y": 0, "z": 0}
    for line in lines:
        cmd, val = line.split()
        val = int(val)
        if cmd == "forward":
            pos["x"] += val
            pos["y"] += pos["z"] * val
        elif cmd == "down":
            pos["z"] += val
        elif cmd == "up":
            pos["z"] -= val
        else:
            raise ValueError("unsupported command: %s", cmd)

    return pos["x"] * pos["y"]
