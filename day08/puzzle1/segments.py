import sys


def main(args):
    input_file = "test_input.txt" if len(args) > 1 else "input.txt"
    with open(input_file, "r") as f:
        count = 0
        for entry in f:
            digits = entry.strip().split("|")[1].strip().split(" ")
            for d in digits:
                if len(d) in [2, 3, 4, 7]:
                    count += 1

    print(f"Number of 1, 4, 7 or 8: {count}")


if __name__ == "__main__":
    main(sys.argv)
