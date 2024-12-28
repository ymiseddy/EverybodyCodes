CardinalDirections = [
    (0, -1),
    (1, 0),
    (0, 1),
    (-1, 0),
]

CardinalDirectionsWithDiagonals = [
    (0, -1),
    (1, -1),
    (1, 0),
    (1, 1),
    (0, 1),
    (-1, 1),
    (-1, 0),
    (-1, -1),
]


class Grid:
    @staticmethod
    def Print(grid: list[list[str]]):
        for row in grid:
            for col in row:
                print(col, end="")
            print()
        print()

    @staticmethod
    def Parse(input: str) -> list[list[str]]:
        lines = input.split("\n")
        grid = []
        for line in lines:
            grid.append(list(line))
        return grid


def PrintMatrix(matrix):
    for row in matrix:
        for col in row:
            print(col, end=" ")
        print()


def Read(filename: str) -> str:
    with open(filename, "r") as f:
        input = f.read()
        input = input.strip()
    return input
