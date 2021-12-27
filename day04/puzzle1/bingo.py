import re
import sys

from collections import defaultdict
from functools import reduce


def read_boards(lines):
    starts = [(i * 5) for i in range(len(lines) // 5)]
    return [read_board(lines[start:start+5]) for start in starts]


def read_board(lines):
    numbers_positions = {}
    for i, line in enumerate(lines):
        for j, n in enumerate(re.sub(" +", " ", line.strip()).split(" ")):
            numbers_positions[int(n)] = (i, j)
    return numbers_positions


def number_location(number, board):
    for i, l in enumerate(board):
        for j, n in enumerate(l):
            if n == number:
                return (i, j)


def main(input_file):
    with open(input_file, "r") as f:
        numbers = [int(n) for n in f.readline().strip().split(",")]
        lines = [l.strip() for l in f.readlines() if l.strip()]
        games = [
            (b, defaultdict(lambda: 0)) for b in read_boards(lines)
        ]
    for n in numbers:
        for (board, r) in games:
            if n in board:
                x, y = board[n]
                del board[n]
                if r[f"l{x}"] == 4 or r[f"c{y}"] == 4:
                    # Finished
                    su = reduce(lambda x, y: x + y, board.keys())
                    score = su * n if board else 0
                    print(f"Winning board is {board}")
                    print(f"Last number is {n}")
                    print(f"Sum of all unmarkedd is {su}")
                    print(f"Final score is {score}")
                    return
                else:
                    r[f"l{x}"] += 1
                    r[f"c{y}"] += 1


if __name__ == "__main__":
    main(sys.argv[1])
