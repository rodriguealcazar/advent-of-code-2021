import sys


def fold(dots, direction, position):
    folded = set()
    for (x, y) in dots:
        if direction == 'x' and x > position:
            x = position - (x - position)
        if direction == 'y' and y > position:
            y = position - (y - position)
        folded.add(f"{x},{y}")
    return folded


def main(input_file):
    coords = []
    with open(input_file, "r") as f:
        for lines in f:
            if lines.strip() and lines[0] != "f":
                x, y = lines.strip().split(",")
                coords.append((int(x), int(y)))
            if lines[0] == "f":
                direction, position = lines[11:].split("=")
                break

    folded = fold(coords, direction, int(position))
    print(f"Number of dots after first fold: {len(folded)}")


if __name__ == "__main__":
    main(sys.argv[1])
