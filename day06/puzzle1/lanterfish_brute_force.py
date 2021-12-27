import sys


def main(args):
    input_file = "test_input.txt" if len(args) > 1 else "input.txt"
    with open(input_file, "r") as f:
        fishes = [int(n) for n in f.readline().strip().split(",")]
    for i in range(256):
        for i in range(len(fishes)):
            if fishes[i] == 0:
                fishes[i] = 6
                fishes.append(8)
            else:
                fishes[i] -= 1

    print(len(fishes))


if __name__ == "__main__":
    main(sys.argv)
