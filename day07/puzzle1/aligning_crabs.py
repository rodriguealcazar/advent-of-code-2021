import sys

from statistics import median


def main(input_file):
    with open(input_file, "r") as f:
        positions = [int(n) for n in f.readline().strip().split(",")]
    aligning = int(median(positions))
    count = 0
    for e in positions:
        count += abs(e - aligning)

    print(f"Fuel used: {count}")


if __name__ == "__main__":
    input_file = "test_input.txt" if len(sys.argv) > 1 else "input.txt"
    main(input_file)
