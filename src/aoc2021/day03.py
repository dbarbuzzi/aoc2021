from typing import List

DATA_PATH = "data/day03-full.txt"


def most_common_value(lines: List[str], pos: int) -> int:
    counts = {"0": 0, "1": 0}
    for line in lines:
        counts[line[pos]] += 1
    if counts["0"] == counts["1"]:
        return 1
    return [0, 1][counts["1"] > counts["0"]]


def least_common_value(lines: List[str], pos: int) -> int:
    return [1, 0][most_common_value(lines, pos)]


def filter_lines(lines: List[str], val: int, pos: int) -> List[str]:
    return [line for line in lines if line[pos] == str(val)]


def part1(data_path=DATA_PATH):
    with open(data_path) as f:
        lines = [line.strip() for line in f if line.strip()]

    half_lines = len(lines) // 2
    num_ones = [0 for _ in range(len(lines[0]))]
    for line in lines:
        for idx, bit in enumerate(line):
            if bit == "1":
                num_ones[idx] += 1

    sig_bits = "".join("1" if num > half_lines else "0" for num in num_ones)
    gamma = int(sig_bits, base=2)
    insig_bits = "".join("0" if num > half_lines else "1" for num in num_ones)
    epsilon = int(insig_bits, base=2)
    return gamma * epsilon


def part2(data_path=DATA_PATH):
    with open(data_path) as f:
        lines = [line.strip() for line in f if line.strip()]

    num_bits = len(lines[0])

    o2_lines = lines.copy()
    for pos in range(num_bits):
        common = most_common_value(o2_lines, pos)
        o2_lines = filter_lines(o2_lines, common, pos)
        if len(o2_lines) == 1:
            o2_bits = o2_lines[0]
            break
    o2 = int(o2_bits, base=2)

    co2_lines = lines.copy()
    for pos in range(num_bits):
        uncommon = least_common_value(co2_lines, pos)
        co2_lines = filter_lines(co2_lines, uncommon, pos)
        if len(co2_lines) == 1:
            co2_bits = co2_lines[0]
            break
    co2 = int(co2_bits, base=2)

    return o2 * co2
