import sys


def main(input_file):
    heightmap = []
    with open(input_file, "r") as f:
        for l in f.readlines():
            heightmap.append([int(n) for n in l.strip()])

    total_risk = 0
    for y, line in enumerate(heightmap):
        for x, height in enumerate(line):
            if x > 0:
                if line[x - 1] <= height:
                    continue
            if x < len(line) - 1:
                if line[x + 1] <= height:
                    continue
            if y > 0:
                if heightmap[y - 1][x] <= height:
                    continue
            if y < len(heightmap) - 1:
                if heightmap[y + 1][x] <= height:
                    continue
            total_risk += height + 1

    print(f"Sum of risk levels is: {total_risk}")


if __name__ == "__main__":
    main(sys.argv[1])
