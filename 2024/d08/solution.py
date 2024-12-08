from collections import defaultdict


def part1(file: str) -> int:
    ans = 0

    with open(file) as f:
        grid = f.read().strip().split("\n")

    rows = len(grid)
    cols = len(grid[0])
    S = defaultdict(list)
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != ".":
                S[grid[r][c]].append((r, c))

    a = set()
    for r in range(rows):
        for c in range(cols):
            for _, vs in S.items():
                for r1, c1 in vs:
                    for r2, c2 in vs:
                        if (r1, c1) != (r2, c2):
                            d1 = abs(r - r1) + abs(c - c1)
                            d2 = abs(r - r2) + abs(c - c2)

                            dr1 = r - r1
                            dr2 = r - r2
                            dc1 = c - c1
                            dc2 = c - c2

                            if (
                                dr1 * dc2 == dc1 * dr2
                                and 0 <= r < rows
                                and 0 <= c < cols
                            ):
                                if d1 == 2 * d2 or d2 == 2 * d1:
                                    a.add((r, c))

    ans = len(a)
    return ans


def part2(file: str) -> int:
    ans = 0

    with open(file) as f:
        grid = f.read().strip().split("\n")

    rows = len(grid)
    cols = len(grid[0])
    S = defaultdict(list)
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != ".":
                S[grid[r][c]].append((r, c))

    a = set()
    for r in range(rows):
        for c in range(cols):
            for _, vs in S.items():
                for r1, c1 in vs:
                    for r2, c2 in vs:
                        if (r1, c1) != (r2, c2):
                            d1 = abs(r - r1) + abs(c - c1)
                            d2 = abs(r - r2) + abs(c - c2)

                            dr1 = r - r1
                            dr2 = r - r2
                            dc1 = c - c1
                            dc2 = c - c2

                            if (
                                dr1 * dc2 == dc1 * dr2
                                and 0 <= r < rows
                                and 0 <= c < cols
                            ):
                                a.add((r, c))

    ans = len(a)
    return ans


print(part1("input.txt"))
print(part2("input.txt"))
