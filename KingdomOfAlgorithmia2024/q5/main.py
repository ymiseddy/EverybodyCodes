import shared as t
import numpy as np


def print_matrix(matrix):
    for row in matrix:
        for col in row:
            print(col, end=" ")
        print()


def part1(input):
    lines = input.split("\n")
    nums = []
    for _, line in enumerate(lines):
        if line == "":
            continue
        parts = line.split(" ")
        x = np.array([int(x) for x in parts])
        nums.append(x)
    # Transpose nums
    nums = np.array(nums)
    nums = np.rot90(nums, k=1)
    nums = np.flip(nums, axis=0)
    nn = []
    for i in range(len(nums)):
        nn.append([])
        for j in range(len(nums[i])):
            nn[i].append(int(nums[i][j]))

    nums = nn

    columns = len(nums)
    rounds = []
    out = ""
    for i in range(10):
        column = i % columns
        next_column = (i + 1) % columns
        # print(f"Round {i+1}: {column}, {next_column}")
        c = nums[column][0]
        nums[column] = nums[column][1:]
        # print(f"{c}")
        # print_matrix(nums)

        length = len(nums[next_column])
        pos = (c - 1) % length
        # print(f"c: {c} length: {length}")
        if c > length:
            if (c // length) % 2 == 1:
                pos = (c + 1) % length
                pos = length - pos

        # push c to next column at position pos
        nums[next_column] = nums[next_column][:pos] + \
            [c] + nums[next_column][pos:]

        # Get the frist column
        col = [nums[x][0] for x in range(len(nums))]

        rounds.append(col)
        out = "".join([str(x) for x in col])

    return out


def part2(input):
    repeats = {}
    lines = input.split("\n")
    nums = []
    for _, line in enumerate(lines):
        if line == "":
            continue
        parts = line.split(" ")
        x = np.array([int(x) for x in parts])
        nums.append(x)
    # Transpose nums
    nums = np.array(nums)
    nums = np.rot90(nums, k=1)
    nums = np.flip(nums, axis=0)
    nn = []
    for round in range(len(nums)):
        nn.append([])
        for j in range(len(nums[round])):
            nn[round].append(int(nums[round][j]))

    nums = nn

    columns = len(nums)
    rounds = []
    out = ""
    round = 0
    while True:
        column = round % columns
        next_column = (round + 1) % columns
        # print(f"Round {round+1}: {column}, {next_column}")
        c = nums[column][0]
        nums[column] = nums[column][1:]
        # print(f"Picked: {c}")
        # print_matrix(nums)

        length = len(nums[next_column])
        pos = (c - 1) % length
        # print(f"c: {c} length: {length}")
        if c > length:
            if ((c - 1) // length) % 2 == 0:
                pos = (c - 1) % length
            else:
                # print("**** odd *****")
                pos = length - (((c % length) - 1) % length)

        # print(f"pos: {pos}")
        # push c to next column at position pos
        nums[next_column] = nums[next_column][:pos] + \
            [c] + nums[next_column][pos:]

        # Get the frist column
        col = [nums[x][0] for x in range(len(nums))]

        rounds.append(col)
        out = "".join([str(x) for x in col])
        r = repeats.get(out, 0)
        repeats[out] = r + 1
        if repeats[out] == 2024:
            break
        # print_matrix(nums)
        # print(f"Round {round + 1}: {out} ({repeats[out]})")
        round += 1

    print(f"Rounds: {round + 1}")
    print(f"Repeats: {out}")
    return int(out) * (round + 1)


def part3(input):
    repeats = {}
    max = 0
    lines = input.split("\n")
    nums = []
    for _, line in enumerate(lines):
        if line == "":
            continue
        parts = line.split(" ")
        x = np.array([int(x) for x in parts])
        nums.append(x)
    # Transpose nums
    nums = np.array(nums)
    nums = np.rot90(nums, k=1)
    nums = np.flip(nums, axis=0)
    nn = []
    for round in range(len(nums)):
        nn.append([])
        for j in range(len(nums[round])):
            nn[round].append(int(nums[round][j]))

    nums = nn

    columns = len(nums)
    rounds = []
    out = ""
    round = 0
    while True:
        column = round % columns
        next_column = (round + 1) % columns
        # print(f"Round {round+1}: {column}, {next_column}")
        c = nums[column][0]
        nums[column] = nums[column][1:]
        # print(f"Picked: {c}")
        # print_matrix(nums)

        length = len(nums[next_column])
        pos = (c - 1) % length
        # print(f"c: {c} length: {length}")
        if c > length:
            if ((c - 1) // length) % 2 == 0:
                pos = (c - 1) % length
            else:
                # print("**** odd *****")
                pos = length - (((c % length) - 1) % length)

        # print(f"pos: {pos}")
        # push c to next column at position pos
        nums[next_column] = nums[next_column][:pos] + \
            [c] + nums[next_column][pos:]

        # Get the frist column
        col = [nums[x][0] for x in range(len(nums))]

        rounds.append(col)
        out = "".join([str(x) for x in col])
        if int(out) > max:
            max = int(out)
        # print_matrix(nums)
        # print(f"Round {round + 1}: {out} ({repeats[out]})")
        round += 1

        if round >= 10_000:
            break

    print(f"Rounds: {round + 1}")
    print(f"Max: {max}")
    return max


if __name__ == "__main__":
    input = t.Read("sample.txt")
    res = part1(input)
    print(f"Part 1 (sample): {res}")

    input = t.Read("input1.txt")
    res = part1(input)
    print(f"Part 1 (sample): {res}")

    input = t.Read("sample2.txt")
    res = part2(input)
    print(f"Part 2 (sample): {res}")

    input = t.Read("input2.txt")
    res = part2(input)
    print(f"Part 2 (input): {res}")

    input = t.Read("input3.txt")
    res = part3(input)
    print(f"Part 3 (input): {res}")
