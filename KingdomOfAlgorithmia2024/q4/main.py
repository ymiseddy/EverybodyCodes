import shared as t
import numpy as np


def part1(input):
    input = input.split("\n")
    # Convert to integers
    input = [int(x) for x in input]
    input = np.array(input)
    min = np.min(input)
    total = sum(input - min)
    return total


def part3(input):
    input = input.split("\n")
    # Convert to integers
    input = [int(x) for x in input]
    input = np.array(input)
    median = np.median(input)
    total = sum(np.abs(input - median))
    return total


if __name__ == "__main__":
    input = t.Read("sample.txt")
    res = part1(input)
    print(f"part 1 res: {res}")

    input = t.Read("input.txt")
    res = part1(input)
    print(f"part (input) 1 res: {res}")

    input = t.Read("input2.txt")
    res = part1(input)
    print(f"part (input) 2 res: {res}")

    input = t.Read("sample3.txt")
    res = part3(input)
    print(f"part (sample) 3 res: {res}")

    input = t.Read("input3.txt")
    res = part3(input)
    print(f"part (input) 3 res: {res}")
