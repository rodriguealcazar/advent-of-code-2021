import sys

from itertools import starmap

totals = []


def matches_at_index(numbers, i):
    most = 0
    zeros = []
    ones = []
    for n in numbers:
        if n[i] == 0:
            zeros.append(n)
            most -= 1
        else:
            ones.append(n)
            most += 1
    return (ones, zeros) if most >= 0 else (zeros, ones)


def oxygen(numbers, i=0):
    if len(numbers) == 1:
        return numbers[0]
    else:
        keep, _ = matches_at_index(numbers, i)
        return oxygen(keep, i + 1)


def co2(numbers, i=0):
    if len(numbers) == 1:
        return numbers[0]
    else:
        _, keep = matches_at_index(numbers, i)
        return co2(keep, i + 1)


def main(input_file):
    with open(input_file, "r") as f:
        numbers = []
        for reading in f:
            bits = list(map(int, reading.strip()))
            numbers.append(bits)
    o = oxygen(numbers, 0)
    c = co2(numbers, 0)
    o = int(''.join(map(str, o)), 2)
    c = int(''.join(map(str, c)), 2)
    print(f"Oxygen: {o}")
    print(f"CO2: {c}")
    print(o * c)


if __name__ == "__main__":
    main(sys.argv[1])
