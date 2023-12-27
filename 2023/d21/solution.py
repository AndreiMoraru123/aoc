from typing import Callable, Tuple


def walk(fn: Callable, start: Tuple[int, int], t: int) -> int:
    bfs = set([start])
    for _ in range(t):
        new_bfs = set()
        breakpoint()
        for i, j in bfs:
            new_bfs.add((i, j - 1))
            new_bfs.add((i, j + 1))
            new_bfs.add((i - 1, j))
            new_bfs.add((i + 1, j))
        new_bfs = {(i, j) for i, j in new_bfs if fn(i, j) == "."}
        bfs = new_bfs
    return len(bfs)


f = open("input.txt")
grid = {(i, j): x for i, line in enumerate(f) for j, x in enumerate(line.strip())}
start = [pos for pos, x in grid.items() if x == "S"].pop()
grid[start] = "."

print(walk(lambda i, j: grid.get((i, j)), start, t=64))
