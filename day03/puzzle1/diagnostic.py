import sys

from itertools import starmap

totals = []

def count(index, bit):
    if len(totals) == index:
        totals.append(0)

    if bit == 0:
       totals[index] -= 1
    else:
       totals[index] += 1


def main(input_file):
    with open(input_file, "r") as f:
        for reading in f:
            bits = list(map(int, reading.strip()))
            list(starmap(count, list(enumerate(bits))))

    gamma_bin = [1 if totals[i] > 0 else 0 for i in range(len(totals))]
    gamma = int(''.join(map(str, gamma_bin)), 2)
    epsilon_bin = [1 if totals[i] < 0 else 0 for i in range(len(totals))]
    epsilon = int(''.join(map(str, epsilon_bin)), 2)

    print(f"gamma: {gamma}")
    print(f"epsilon: {epsilon}")
    print(gamma * epsilon)


if __name__ == "__main__":
    main(sys.argv[1])
