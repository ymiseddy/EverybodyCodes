import shared as t


def part1(input):
    # Iterate over grid
    grid = t.Grid.Parse(input)

    total = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == "#":
                total += 1
                grid[y][x] = str(1)
    current = 1
    next = 2
    while True:
        dug = False
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] != str(current):
                    continue
                for direction in t.CardinalDirections:
                    dx = x + direction[0]
                    dy = y + direction[1]
                    if (dx < 0 or
                            dy < 0 or
                            dx >= len(grid[y]) or
                            dy >= len(grid)):
                        break

                    if (grid[dy][dx] != str(current)
                            and grid[dy][dx] != str(next)):
                        break
                else:
                    total += 1
                    dug = True
                    grid[y][x] = str(next)
        next += 1
        current += 1

        if not dug:
            break
        # t.Grid.Print(grid)
    return total


def part3(input):
    grid = t.Grid.Parse(input)
    # t.Grid.Print(grid)

    # Iterate over grid
    total = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == "#":
                total += 1
                grid[y][x] = str(1)

    # t.Grid.Print(grid)
    current = 1
    next = 2
    while True:
        dug = False
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] != str(current):
                    continue
                for direction in t.CardinalDirectionsWithDiagonals:
                    dx = x + direction[0]
                    dy = y + direction[1]
                    if (dx < 0 or
                            dy < 0 or
                            dx >= len(grid[y]) or
                            dy >= len(grid)):
                        break

                    if (grid[dy][dx] != str(current) and
                            grid[dy][dx] != str(next)):
                        break
                else:
                    total += 1
                    dug = True
                    grid[y][x] = str(next)
        next += 1
        current += 1

        if not dug:
            break
    return total


if __name__ == "__main__":  # Read input.txt
    # Read input.txt
    input = t.Read("input.txt")
    res = part1(input)
    print(f"part 1 res: {res}")

    input = t.Read("input2.txt")
    res = part1(input)
    print(f"part 2 res: {res}")

    input = t.Read("input3.txt")
    input = input.strip()
    res = part3(input)
    print(f"part 3 res: {res}")
