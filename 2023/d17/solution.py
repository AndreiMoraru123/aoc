from collections import defaultdict
from heapq import heappop, heappush
from typing import Callable, Dict, Tuple


def dijkstra(
    grid: Dict[Tuple[int, int], int],
    start: Tuple[int, int],
    end: Tuple[int, int],
    neighbors: Callable,
    max_run: int,
):
    s = start, (0, 0)
    dist = defaultdict(lambda: float("inf"), {s: 0})
    prio_queue = [(0, s)]
    while prio_queue:
        _, u = heappop(prio_queue)
        if not all(-max_run <= n <= max_run for n in u[1]):
            continue
        if u[0] == end:
            return dist[u]
        for v in neighbors(*u):
            if v[0] not in grid:
                continue
            alt = dist[u] + grid[v[0]]
            if alt < dist[v]:
                dist[v] = alt
                heappush(prio_queue, (alt, v))


def neighbors1(pos: Tuple[int, int], run: Tuple[int, int]):
    row, col = pos
    n_row, n_col = run
    if n_row == 0:  # has not moved verically
        yield (row - 1, col), (-1, 0)  # can move up
        yield (row + 1, col), (1, 0)  # can move down
    if n_col == 0:  # has not moved horizontally
        yield (row, col - 1), (0, -1)  # can move left
        yield (row, col + 1), (0, 1)  # can move down
    if n_row > 0:  # has been moving down
        yield (row + 1, col), (n_row + 1, 0)  # can keep moving down
    if n_row < 0:  # has been moving up
        yield (row - 1, col), (n_row - 1, 0)  # can keep moving up
    if n_col > 0:  # has been moving right
        yield (row, col + 1), (0, n_col + 1)  # can keep moving right
    if n_col < 0:  # has been moving left
        yield (row, col - 1), (0, n_col - 1)  # can keep moving left

def neighbors2(pos: Tuple[int, int], run: Tuple[int, int]):
    row, col = pos
    n_row, n_col = run
    if 0 < n_row < 4:  # has been moving down & has not reached minimum of 4 steps
        yield (row + 1, col), (n_row + 1, 0)  # can keep moving down
    elif -4 <= n_row < 0:  # has been moving up & has not reached minimum of 4 steps
        yield (row - 1, col), (n_row - 1, 0)  # can keep moving up
    elif 0 < n_col < 4:  # has been moving right & has not reached minimum of 4 steps
        yield (row, col + 1), (0, n_col + 1)  # can keep moving right
    elif -4 < n_col < 0:  # has been moving left & has not reached minimum of 4 steps
        yield (row, col - 1), (0, n_col - 1)  # can keep moving left
    else:
        yield from neighbors1(pos, run)


lines = open("input.txt").read().splitlines()
grid = {(i, j): int(x) for i, line in enumerate(lines) for j, x in enumerate(line)}
rows, cols = len(lines), len(lines[0])

print(dijkstra(grid, (0, 0), (rows - 1, cols - 1), neighbors1, max_run=3))
print(dijkstra(grid, (0, 0), (rows - 1, cols - 1), neighbors2, max_run=10))
