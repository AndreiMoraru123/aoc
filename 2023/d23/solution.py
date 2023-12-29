import sys
from typing import Tuple

sys.setrecursionlimit(2**31 - 1)
visited = set()


def neighbors(i: int, j: int):
    yield i - 1, j
    yield i + 1, j
    yield i, j - 1
    yield i, j + 1


def dfs_slopes(pos: Tuple[int, int], rows: int, cols: int) -> int:
    if pos == (rows - 1, cols - 2):
        return 0
    visited.add(pos)
    ans = -1
    nb = list(neighbors(*pos))
    if grid[pos] in "^v<>":
        nb = [nb["^v<>".index(grid[pos])]]
    for n in nb:
        if n not in grid or n in visited:
            continue
        ans = max(ans, 1 + dfs_slopes(n, rows, cols))
    visited.remove(pos)
    return ans


def dfs(pos: Tuple[int, int], rows: int, cols: int) -> int:
    if pos == (rows - 1, cols - 2):
        return 0
    visited.add(pos)
    ans = - 10 ** 3
    for n, dist in adj[pos].items():
        if n in visited:
            continue
        ans = max(ans, dist + dfs(n, rows, cols))
    visited.remove(pos)
    return ans

lines = open("input.txt").read().splitlines()
rows, cols = len(lines), len(lines[0])
grid = {
    (i, j): x for i, line in enumerate(lines) for j, x in enumerate(line) if x != "#"
}

adj = {p : {q: 1 for q in neighbors(*p) if q in grid} for p in grid}

while True:
    for p, qs in adj.items():
        if len(qs) != 2:
            continue
        q1, q2 = adj[p]
        adj[q1][q2] = adj[q2][q1] = adj[q1][p] + adj[p][q2]
        del adj[p], adj[q1][p], adj[q2][p]
        break
    else:
        break


visited = set()
print(dfs_slopes((0, 1), rows, cols))

visited = set()
print(dfs((0, 1), rows, cols))
