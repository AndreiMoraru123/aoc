import numpy as np
from typing import Callable, Tuple


def walk(fn: Callable, start: Tuple[int, int], t: int) -> int:
    bfs = set([start])
    for _ in range(t):
        new_bfs = set()
        for i, j in bfs:
            new_bfs.add((i, j - 1))
            new_bfs.add((i, j + 1))
            new_bfs.add((i - 1, j))
            new_bfs.add((i + 1, j))
        new_bfs = {(i, j) for i, j in new_bfs if fn(i, j) == "."}
        bfs = new_bfs
    return len(bfs)


f = open("input.txt")
lines = f.read().splitlines()
n, m = len(lines), len(lines[0])

grid = {(i, j): x for i, line in enumerate(lines) for j, x in enumerate(line.strip())}
start = [pos for pos, x in grid.items() if x == "S"].pop()
grid[start] = "."

print(walk(lambda i, j: grid.get((i, j)), start, t=64))

get = lambda i, j: grid[i % n, j % m]
step_count = 26501365

s1 = step_count % n
p1 = walk(get, start, s1)
s2 = step_count % n + n
p2 = walk(get, start, s2)
s3 = step_count % n + 2 * n
p3 = walk(get, start, s3)
s4 = step_count % n + 3 * n
p4 = walk(get, start, s4)

steps = np.array([s1, s2, s3, s4])
plots = np.array([p1, p2, p3, p4])

coefficients = np.polyfit(steps, plots, 2)
prediction = np.polyval(coefficients, step_count)
print(int(prediction))
