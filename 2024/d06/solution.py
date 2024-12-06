def part1(file: str) -> int:
    ans = 0
    with open(file) as f:
        grid = f.read().strip().split("\n")
        rows = len(grid)
        cols = len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "^":
                    sr, sc = r, c

        for wr in range(rows):
            for wc in range(cols):
                r, c = sr, sc
                seen = set()
                seen_rc = set()
                d = 0  # 0: up, 1: right, 2: down, 3: left

                while True:
                    if (r, c, d) in seen:
                        break
                    seen.add((r, c, d))
                    seen_rc.add((r, c))
                    dr, dc = [(-1, 0), (0, 1), (1, 0), (0, -1)][d]
                    rr = r + dr
                    cc = c + dc

                    if not (0 <= rr < rows and 0 <= cc < cols):
                        if grid[wr][wc] == "#":
                            ans = len(seen_rc)
                        break

                    if grid[rr][cc] == "#" or rr == wr and cc == wc:
                        d = (d + 1) % 4  # turn right
                    else:
                        r, c = rr, cc  # move forward

    return ans


def part2(file: str) -> int:
    ans = 0
    with open(file) as f:
        grid = f.read().strip().split("\n")
        rows = len(grid)
        cols = len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "^":
                    sr, sc = r, c

        for wr in range(rows):
            for wc in range(cols):
                r, c = sr, sc
                seen = set()
                d = 0  # 0: up, 1: right, 2: down, 3: left

                while True:
                    if (r, c, d) in seen:
                        ans += 1
                        break
                    seen.add((r, c, d))
                    dr, dc = [(-1, 0), (0, 1), (1, 0), (0, -1)][d]
                    rr = r + dr
                    cc = c + dc

                    if not (0 <= rr < rows and 0 <= cc < cols):
                        break

                    if grid[rr][cc] == "#" or rr == wr and cc == wc:
                        d = (d + 1) % 4  # turn right
                    else:
                        r, c = rr, cc  # move forward

    return ans


print(part1("input.txt"))
print(part2("input.txt"))
