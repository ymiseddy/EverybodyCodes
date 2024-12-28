import shared as t


path_lengths = {}


def dfs(graph, start, visited, path):
    if start == "@":
        print(f"start: {start}, visited: {visited}, path: {path}")
        pathKey = "".join(path)
        path_lengths[pathKey] = len(path)
        return

    if start not in graph:
        return

    visited.append(start)
    for edge in graph[start]:
        if edge not in visited:
            path.append(edge)
            dfs(graph, edge, visited, path)
            path.pop()


def part1(input):
    global path_lengths
    path_lengths = {}
    input = input.split("\n")
    edgeDict = {}
    for line in input:
        start, edgestr = line.split(":")
        edges = edgestr.split(",")
        edgeDict[start] = edges

    # Look for a path with the shortest unique length
    start = "RR"
    dfs(edgeDict, start, [], [start])
    print(f"path_lengths: {path_lengths}")
    countPaths = {}
    for k, v in path_lengths.items():
        if v not in countPaths:
            countPaths[v] = []
        countPaths[v].append(k)

    minPath = ""
    for k, v in countPaths.items():
        if len(v) == 1:
            minPath = v[0]
            break

    return minPath


def dfs2(graph, start, visited, path):
    if start == "@":
        pathKey = ",".join(path)
        path_lengths[pathKey] = len(path)
        return

    if start not in graph:
        return

    visited.append(start)
    for edge in graph[start]:
        if edge not in visited:
            path.append(edge)
            dfs2(graph, edge, visited, path)
            path.pop()


def part2(input):
    global path_lengths
    path_lengths = {}
    input = input.split("\n")
    edgeDict = {}
    for line in input:
        start, edgestr = line.split(":")
        edges = edgestr.split(",")
        edgeDict[start] = edges

    # Look for a path with the shortest unique length
    start = "RR"
    dfs2(edgeDict, start, [], [start])
    print(f"path_lengths: {path_lengths}")
    countPaths = {}
    for k, v in path_lengths.items():
        if v not in countPaths:
            countPaths[v] = []
        countPaths[v].append(k)

    minPath = ""
    for k, v in countPaths.items():
        if len(v) == 1:
            minPath = v[0]
            break

    words = minPath.split(",")
    word = ""
    for i in words:
        word += i[0]

    return word


if __name__ == "__main__":

    input = t.Read("input.txt")
    res = part1(input)
    print(f"Part 1 (input): {res}")

    input = t.Read("input.txt")
    res = part1(input)
    print(f"Part 1 (input): {res}")

    input = t.Read("input2.txt")
    res = part2(input)
    print(f"Part 2 (input): {res}")

    input = t.Read("input3.txt")
    res = part2(input)
    print(f"Part 2 (input): {res}")
