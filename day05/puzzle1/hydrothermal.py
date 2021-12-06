import sys

from collections import defaultdict


def main(args):
    input_file = "test_input.txt" if len(args) > 1 else "input.txt"

    diagram = defaultdict(lambda: 0)
    with open(input_file, "r") as f:
        for line in f:
            if not line.strip():
                continue
            xs, ys, xe, ye = [
                int(n) for coord in line.strip().split(" -> ")
                for n in coord.split(",")
            ]
            if xs == xe:
                min_y = min(ys, ye)
                max_y = max(ys, ye)
                for j in range(min_y, max_y + 1):
                    diagram[f'{xs}:{j}'] += 1
            elif ys == ye:
                min_x = min(xs, xe)
                max_x = max(xs, xe)
                for i in range(min_x, max_x + 1):
                    diagram[f'{i}:{ys}'] += 1

    overlaps = 0
    for coords in diagram.values():
        if coords > 1:
            overlaps += 1
    print(overlaps)


if __name__ == "__main__":
    main(sys.argv)
