from typing import List, Tuple

DATA_PATH = "data/day04-full.txt"


def load_data(fn: str) -> Tuple[List[str], List[List[List[str]]]]:
    with open(fn) as f:
        groups = [group.strip().split("\n") for group in f.read().split("\n\n")]
    called = groups[0][0].split(",")
    boards = []
    for group in groups[1:]:
        board = list(map(lambda line: line.split(), group))
        boards.append(board)
    return called, boards


def mark_board(board: List[List[str]], num: str) -> List[List[str]]:
    for a, row in enumerate(board):
        for b, cell in enumerate(row):
            if cell == num:
                board[a][b] = "0"
    return board


def mark_boards(boards: List[List[List[str]]], num: str) -> List[List[List[str]]]:
    return [mark_board(board, num) for board in boards]


def check_board(board: List[List[str]]) -> bool:
    cols = [[], [], [], [], []]
    for row in board:
        if set(row) == {"0"}:
            return True
        for y, cell in enumerate(row):
            cols[y].append(cell)
    return any(set(col) == {"0"} for col in cols)


def check_boards(boards: List[List[List[str]]]) -> List[List[List[str]]]:
    return [board for board in boards if check_board(board)]


def filter_winners(boards: List[List[List[str]]]) -> List[List[List[str]]]:
    return [board for board in boards if not check_board(board)]


def sum_unmarked(board: List[List[str]]) -> int:
    un_sum = 0
    for row in board:
        for cell in row:
            un_sum += int(cell)
    return un_sum


def part1(data_path: str = DATA_PATH) -> int:
    called, boards = load_data(data_path)
    for num in called:
        boards = mark_boards(boards, num)
        bingos = check_boards(boards)
        if bingos:
            break

    # assume there's only one bingo...
    unmarked = sum_unmarked(bingos[0])
    return int(num) * unmarked


def part2(data_path: str = DATA_PATH) -> int:
    called, boards = load_data(data_path)
    for num in called:
        boards = mark_boards(boards, num)
        if len(boards) > 1:
            boards = filter_winners(boards)
        elif check_board(boards[0]):
            break

    unmarked = sum_unmarked(boards[0])
    return int(num) * unmarked
