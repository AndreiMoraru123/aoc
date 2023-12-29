import sys
from typing import Tuple

sys.setrecursionlimit(2**31 - 1)
visited = set()


def neighbors(i: int, j: int):
    yield i - 1, j
    yield i + 1, j
    yield i, j - 1
    yield i, j + 1


def dfs(pos: Tuple[int, int], rows: int, cols: int) -> int:
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
        ans = max(ans, 1 + dfs(n, rows, cols))
    visited.remove(pos)
    return ans


lines = open("input.txt").read().splitlines()
rows, cols = len(lines), len(lines[0])
grid = {
    (i, j): x for i, line in enumerate(lines) for j, x in enumerate(line) if x != "#"
}
visited = set()

print(dfs((0, 1), rows, cols))
