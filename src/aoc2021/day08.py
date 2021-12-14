from typing import List, Tuple

DATA_PATH = "data/day08-full.txt"


def load_data(fp: str) -> List[Tuple[List[set], List[set]]]:
    with open(fp) as f:
        data = [line.strip() for line in f if line.strip()]
    res = []
    for line in data:
        signals, values = line.split(" | ")
        ss = list(map(set, signals.split()))
        sv = list(map(set, values.split()))
        res.append((ss, sv))
    return res


def determine_five_seg_num(segments: set, one: set, four: set) -> int:
    # numbers 2, 3, and 5 each have five segments
    if len(segments & one) == 2:
        # intersection of segments with num-1 contains two segments: 3
        return 3
    elif len(segments & four) == 3:
        # else intersection of segments with num-4 contains three segments: 5
        return 5
    else:
        # else: 2
        return 2


def determine_six_seg_num(segments: set, one: set, four: set) -> int:
    # numbers 0, 6, and 9 each have six segments
    if len(segments & one) == 1:
        # intersection of segments with num-1 contains 1 segment: 6
        return 6
    elif len(segments & four) == 4:
        # else intersection of segments with num-4 contains 4 segments: 9
        return 9
    else:
        # else: 0
        return 0


def generate_seq_map(signals: List[set]) -> List[set]:
    mapping = [0] * 10
    unknowns: List[set] = []

    # first pass to determine known reference points
    for s in signals:
        if len(s) == 2:
            mapping[1] = s
        elif len(s) == 3:
            mapping[7] = s
        elif len(s) == 4:
            mapping[4] = s
        elif len(s) == 7:
            mapping[8] = s
        else:
            unknowns.append(s)

    # second pass to use ref points to deduce remaining unknowns
    for s in unknowns:
        if len(s) == 5:
            res = determine_five_seg_num(s, mapping[1], mapping[4])
            mapping[res] = s
        elif len(s) == 6:
            res = determine_six_seg_num(s, mapping[1], mapping[4])
            mapping[res] = s

    return mapping


def part1(data_path: str = DATA_PATH) -> int:
    lines = load_data(data_path)
    return sum(sum(len(v) in {2, 3, 4, 7} for v in values) for _, values in lines)


def part2(data_path: str = DATA_PATH) -> int:
    lines = load_data(data_path)
    total = 0
    for signals, values in lines:
        mapping = generate_seq_map(signals)
        total += sum(
            10 ** i * mapping.index(value) for i, value in enumerate(reversed(values))
        )
    return total
