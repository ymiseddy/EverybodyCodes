import shared as t
import math
import itertools as it
import numpy as np


def part1(input):
    input = input.split("\n")
    idOpsDict = {}
    for line in input:
        id, ops = line.split(":")
        ops = ops.split(",")
        delta = 0
        opList = []
        for op in ops:
            if op == "+":
                delta = 1
            elif op == "-":
                delta = -1
            elif op == "=":
                delta = 0
            else:
                raise ValueError(f"Invalid op: {op}")
            opList.append(delta)
        idOpsDict[id] = opList

    results = []
    for k, v in idOpsDict.items():
        initial = 10
        total = 0
        for x in range(10):
            op = v[x % len(v)]
            initial += op
            if initial < 0:
                initial = 0

            total += initial
        results.append((k, total))
    # Sort by initial in descending order
    results = sorted(results, key=lambda x: x[1], reverse=True)
    result = "".join([x[0] for x in results])

    return result


def trace_track(track_lines):
    sx = 0
    sy = 0
    t.CardinalDirections
    if track_lines[sy][sx] != "S":
        raise ValueError("Track does not start with S")

    c = 0
    track = []
    prevDirection = 0  # Start at up
    while True:
        if c > 0 and track_lines[sy][sx] == "S":
            break
        c += 1
        track.append(track_lines[sy][sx])
        for x, direction in enumerate(t.CardinalDirections):

            # Don't go back
            if x == (prevDirection + 2) % len(t.CardinalDirections):
                continue

            dx = sx + direction[0]
            dy = sy + direction[1]
            if (dx < 0 or dy < 0 or
                    dx >= len(track_lines[sy]) or
                    dy >= len(track_lines)):
                continue
            if track_lines[dy][dx] != " ":
                prevDirection = x
                sx = dx
                sy = dy
                break
        else:
            raise ValueError("No path found")
    return "".join(track)


# Incorrect: DIGCAEFKB
#            DIGCAEKFB
def sim_run(track, operations, loops=10):
    initial = 10
    total = 0
    for x in range(loops * len(track)):
        p = (x + 1) % len(track)
        op = operations[x % len(operations)]
        c = track[p]
        if c == "+":
            initial += 1
        elif c == "-":
            initial -= 1
        elif c == "=" or c == "S":
            initial += op
        total += initial
    return total


def part2(input):
    plan, track = input.split("\n\n")
    idOpsDict = {}
    plan = plan.split("\n")
    for line in plan:
        id, ops = line.split(":")
        ops = ops.split(",")
        delta = 0
        opList = []
        for op in ops:
            if op == "+":
                delta = 1
            elif op == "-":
                delta = -1
            elif op == "=":
                delta = 0
            else:
                raise ValueError(f"Invalid op: {op}")
            opList.append(delta)
        idOpsDict[id] = opList

    track_lines = track.split("\n")
    track = trace_track(track_lines)

    results = []
    for id, operations in idOpsDict.items():
        total = sim_run(track, operations)
        results.append((id, total))

    # Sort by initial in descending order
    results = sorted(results, key=lambda x: x[1], reverse=True)
    result = "".join([x[0] for x in results])

    return result


def search_strategies(track, target, loops):
    availableActions = list("+++++---===")
    opList = []
    for op in availableActions:
        if op == "+":
            delta = 1
        elif op == "-":
            delta = -1
        elif op == "=":
            delta = 0
        else:
            raise ValueError(f"Invalid op: {op}")
        opList.append(delta)
    print("Generating all permutations")
    perms = set(it.permutations(opList))
    print(f"perms: {len(perms)}")
    total = 0
    for i in perms:
        run = sim_run(track, i, loops)
        if run > target:
            total += 1
    return total


def part3(input):
    plan, track = input.split("\n\n")
    idOpsDict = {}
    plan = plan.split("\n")
    for line in plan:
        id, ops = line.split(":")
        ops = ops.split(",")
        delta = 0
        opList = []
        for op in ops:
            if op == "+":
                delta = 1
            elif op == "-":
                delta = -1
            elif op == "=":
                delta = 0
            else:
                raise ValueError(f"Invalid op: {op}")
            opList.append(delta)
        idOpsDict[id] = opList
    track_lines = track.split("\n")
    track = trace_track(track_lines)
    track_len = len(track)
    max_ops = 11

    # Compute least common multiple
    # I was hoping this would be smaller than 2024.
    lcm = abs(track_len*max_ops) // math.gcd(track_len, max_ops)

    print(f"lcm: {lcm}")
    print(idOpsDict)
    competitor = idOpsDict["A"]
    run = sim_run(track, competitor, 11)
    s = search_strategies(track, run, 11)
    return s


if __name__ == "__main__":
    input = t.Read("sample.txt")
    res = part1(input)
    print(f"Part 1 (sample): {res}")

    input = t.Read("input.txt")
    res = part1(input)
    print(f"Part 1 (input): {res}")

    input = t.Read("sample2.txt")
    res = part2(input)
    print(f"Part 2 (sample): {res}")

    input = t.Read("input2.txt")
    res = part2(input)
    print(f"Part 2 (input): {res}")

    input = t.Read("input3.txt")
    res = part3(input)
    print(f"Part 3 (input): {res}")
