def neighbors(pos: Tuple[int, int], grid: List[List[int]]) -> List[Tuple[int, int]]:
    r, c = pos
    rows, cols = len(grid), len(grid[0])
    ns = []

    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols:
            ns.append((nr, nc))
    return ns


def find_peaks(start: Tuple[int, int], grid: List[List[int]]) -> Set[Tuple[int, int]]:
    peaks = set()

    def dfs(pos: Tuple[int, int], curr: int) -> None:
        if grid[pos[0]][pos[1]] == 9:
            peaks.add(pos)
            return

        for p in neighbors(pos, grid):
            h = grid[p[0]][p[1]]
            if h == curr + 1:
                dfs(p, h)

    dfs(start, 0)
    return peaks


def count_paths(start: Tuple[int, int], grid: List[List[int]]) -> int:
    paths = 0

    def dfs(pos: Tuple[int, int], curr: int) -> None:
        nonlocal paths
        if grid[pos[0]][pos[1]] == 9:
            paths += 1
            return

        for p in neighbors(pos, grid):
            h = grid[p[0]][p[1]]
            if h == curr + 1:
                dfs(p, h)

    dfs(start, 0)
    return paths


def part1(file: str) -> int:
    ans = 0
    with open(file) as f:
        grid = [[int(c) for c in line.strip()] for line in f]
    rows = len(grid)
    cols = len(grid[0])
    heads = []
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0:
                heads.append((r, c))

    for head in heads:
        peaks = find_peaks(head, grid)
        ans += len(peaks)
    return ans


def part2(file: str) -> int:
    ans = 0
    with open(file) as f:
        grid = [[int(c) for c in line.strip()] for line in f]
    rows = len(grid)
    cols = len(grid[0])
    heads = []
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0:
                heads.append((r, c))

    for head in heads:
        num_paths = count_paths(head, grid)
        ans += num_paths
    return ans


print(part1("input.txt"))
print(part2("input.txt"))
