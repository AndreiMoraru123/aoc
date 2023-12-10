from typing import List, Tuple, Deque
from collections import deque


class SmartTuple(tuple):
    def __add__(self, other):
        return SmartTuple(x + y for x, y in zip(self, other))

    def __neg__(self):
        return SmartTuple(-x for x in self)


directions = {
    "right": (0, 1),
    "left": (0, -1),
    "down": (1, 0),
    "up": (-1, 0),
}

pipe_logic = {
    ".": [],
    "|": [directions["down"], directions["up"]],
    "-": [directions["right"], directions["left"]],
    "L": [directions["right"], directions["up"]],
    "J": [directions["left"], directions["up"]],
    "7": [directions["left"], directions["down"]],
    "F": [directions["right"], directions["down"]],
}


def is_valid_position(sketch: List[List[str]], position: SmartTuple) -> bool:
    i, j = position
    return 0 <= i < len(sketch) and 0 <= j < len(sketch[0])


def get_pipe(sketch: List[List[str]], position: SmartTuple) -> str:
    if is_valid_position(sketch, position):
        i, j = position
        return sketch[i][j]
    return "."


pipe_logic = {k: [SmartTuple(x) for x in v] for k, v in pipe_logic.items()}
connectors = pipe_logic["|"] + pipe_logic["-"]

f = open("input.txt")

sketch = [list(line.strip()) for line in f]
s = [
    SmartTuple((i, j))
    for i in range(len(sketch))
    for j in range(len(sketch[0]))
    if sketch[i][j] == "S"
].pop()
# check adjancency to S by looking if the opposite direction gets back to S
s_dir = [conn for conn in connectors if -conn in pipe_logic[get_pipe(sketch, s + conn)]]

# find the type of pipe S is by trying to find what type would match it's possible connections
sketch[s[0]][s[1]] = next(
    pipe for pipe, directions in pipe_logic.items() if set(directions) == set(s_dir)
)
print("Starting position = ", sketch[s[0]][s[1]])

bfs: Deque[Tuple[SmartTuple, int]] = deque([(s, 0)])
dists = {}
while bfs:
    pipe, dist = bfs.popleft()
    if not is_valid_position(sketch, pipe) or pipe in dists:
        continue
    dists[pipe] = dist
    for adjancent_pipe in pipe_logic[sketch[pipe[0]][pipe[1]]]:
        bfs.append((pipe + adjancent_pipe, dist + 1))

print(max(dists.values()))

EXPANDS = {
    ".": ["...", "...", "..."],
    "|": [".#.", ".#.", ".#."],
    "-": ["...", "###", "..."],
    "L": [".#.", ".##", "..."],
    "J": [".#.", "##.", "..."],
    "7": ["...", "##.", ".#."],
    "F": ["...", ".##", ".#."],
}

expanded_grid_size = len(sketch) * 3, len(sketch[0]) * 3
expanded_grid = [
    ["." for _ in range(expanded_grid_size[1])] for _ in range(expanded_grid_size[0])
]

for i in range(len(sketch)):
    for j in range(len(sketch[0])):
        exp = EXPANDS[sketch[i][j]]
        for ei in range(3):
            for ej in range(3):
                expanded_grid[i * 3 + ei][j * 3 + ej] = exp[ei][ej]

bfs: Deque[SmartTuple] = deque([SmartTuple((0, 0))])
seen = set()
while bfs:
    pipe = bfs.popleft()
    if (
        not is_valid_position(expanded_grid, pipe)
        or pipe in seen
        or expanded_grid[pipe[0]][pipe[1]] == "#"
    ):
        continue
    seen.add(pipe)
    for conn in connectors:
        bfs.append(pipe + SmartTuple(conn))

# not seen == not reacheable via BFS traversal == inside the loop
enclosed_tiles = [
    all((i * 3 + ei, j * 3 + ej) not in seen for ei in range(3) for ej in range(3))
    for i in range(len(sketch))
    for j in range(len(sketch[i]))
]

print(sum(enclosed_tiles))
