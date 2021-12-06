import re
import sys

from collections import defaultdict
from functools import reduce


def read_boards(lines):
    starts = [(i * 5) for i in range(len(lines) // 5)]
    return [read_board(lines[start:start+5]) for start in starts]


def read_board(lines):
    board = []
    bag = set()
    for line in lines:
        l = []
        for n in re.sub(" +", " ", line.strip()).split(" "):
            number = int(n)
            l.append(number)
            bag.add(number)
        board.append(l)
    return (board, bag)


def number_location(number, board):
    for i, l in enumerate(board):
        for j, n in enumerate(l):
            if n == number:
                return (i, j)


def main(args):
    input_file = "test_input.txt" if len(args) > 1 else "input.txt"
    with open(input_file, "r") as f:
        numbers = [int(n) for n in f.readline().strip().split(",")]
        lines = [l.strip() for l in f.readlines() if l.strip()]
        games = [
            (b, s, defaultdict(lambda: 0)) for (b, s) in read_boards(lines)
        ]
    for n in numbers:
        for (b, s, r) in games:
            loc = number_location(n, b)
            if loc:
                s.remove(n)
                if r[f"l{loc[0]}"] == 4 or r[f"c{loc[1]}"] == 4:
                    # Finished
                    su = reduce(lambda x, y: x + y, s)
                    score = su * n if s else 0
                    print(f"Winning board is {b}")
                    print(f"Last number is {n}")
                    print(f"Sum of all unmarkedd is {su}")
                    print(f"Final score is {score}")
                    return
                else:
                    r[f"l{loc[0]}"] += 1
                    r[f"c{loc[1]}"] += 1


if __name__ == "__main__":
    main(sys.argv)
