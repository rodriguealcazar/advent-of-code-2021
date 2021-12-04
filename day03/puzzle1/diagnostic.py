from itertools import starmap

ones = []
zeros = []

def count(index, bit):
    i = int(bit)

    if len(ones) == index:
        ones.append(0)
        zeros.append(0)

    if bit == 0:
        zeros[index] += 1
    else:
        ones[index] += 1

with open("input.txt", "r") as f:
    for reading in f:
        bits = list(map(int, reading.strip()))
        list(starmap(count, list(enumerate(bits))))

gamma_bin = [1 if ones[i] > zeros[i] else 0 for i in range(len(ones))]
gamma = int(''.join(map(str, gamma_bin)), 2)
epsilon_bin = [1 if zeros[i] > ones[i] else 0 for i in range(len(ones))]
epsilon = int(''.join(map(str, epsilon_bin)), 2)

print(f"gamma: {gamma}")
print(f"epsilon: {epsilon}")
print(gamma * epsilon)
