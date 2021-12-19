import sys

from collections import defaultdict



def diagonal(diagram, xs, xe, ys, ye):
    for i in range(abs(xs - xe) + 1):
        x = xs + i if xs < xe else xs - i
        y = ys + i if ys < ye else ys - i
        diagram[f'{x}:{y}'] += 1


def main(input_file):
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
            else:
                diagonal(diagram, xs, xe, ys, ye)


    overlaps = 0
    for coords in diagram.values():
        if coords > 1:
            overlaps += 1
    print(overlaps)


if __name__ == "__main__":
    main(sys.argv[1])
