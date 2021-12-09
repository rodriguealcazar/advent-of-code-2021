import sys

from collections import defaultdict


already_computed = {}

def number_after(left, days):
    if left >= days:
        return 1
    else:
        spawn_day = days - (left + 1)
        if spawn_day not in already_computed:
            already_computed[spawn_day] = number_after(6, spawn_day)
        if spawn_day - 2 not in already_computed:
            already_computed[spawn_day - 2] = number_after(6, spawn_day - 2)

        return already_computed[spawn_day] + already_computed[spawn_day -2 ]


def main(args):
    input_file = "test_input.txt" if len(args) > 1 else "input.txt"
    fishes = defaultdict(lambda: 0)
    with open(input_file, "r") as f:
        for fish in f.readline().strip().split(","):
            fishes[int(fish)] += 1
    total = 0
    for f, c in fishes.items():
        total += c * number_after(f, 256)

    print(f"Final number of fishes: {total}")


if __name__ == "__main__":
    main(sys.argv)
