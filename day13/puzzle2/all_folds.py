import sys

from colorama import Cursor


def folded(dots, direction, position):
    folded = set()
    for (x, y) in dots:
        if direction == 'x' and x > position:
            x = position - (x - position)
        if direction == 'y' and y > position:
            y = position - (y - position)
        folded.add((x, y))
    return folded


def folded_completely(coords, folds):
    for (d, p) in folds:
        coords = folded(coords, d, p)
    return coords


def main(input_file):
    coords = set()
    folds = []
    with open(input_file, "r") as f:
        for l in f:
            if l.strip() and l[0] != "f":
                x, y = l.strip().split(",")
                coords.add((int(x), int(y)))
            if l[0] == "f":
                d, p = l[11:].split("=")
                folds.append((d, int(p)))

    folded = folded_completely(coords, folds)

    for (x, y) in folded:
        print(f"{Cursor.POS(x + 1, y + 4)}#")
    print()
    print()
    print()



if __name__ == "__main__":
    main(sys.argv[1])
