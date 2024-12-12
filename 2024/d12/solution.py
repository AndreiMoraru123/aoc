from collections import deque


def part1(file: str) -> int:
    ans = 0
    with open(file) as f:
        region = f.read().strip().split("\n")

    rows = len(region)
    cols = len(region[0])

    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    seen = set()
    for r in range(rows):
        for c in range(cols):
            if (r, c) in seen:
                continue
            Q = deque([(r, c)])
            area = 0
            perim = 0
            while Q:
                r2, c2 = Q.popleft()
                if (r2, c2) in seen:
                    continue
                seen.add((r2, c2))
                area += 1
                for dr, dc in dirs:
                    rr = r2 + dr
                    cc = c2 + dc
                    if (
                        0 <= rr < rows
                        and 0 <= cc < cols
                        and region[rr][cc] == region[r2][c2]
                    ):
                        Q.append((rr, cc))
                    else:
                        perim += 1
            ans += area * perim
    return ans


def part2(file: str) -> int:
    ans = 0
    with open(file) as f:
        region = f.read().strip().split("\n")

    rows = len(region)
    cols = len(region[0])

    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    seen = set()
    for r in range(rows):
        for c in range(cols):
            if (r, c) in seen:
                continue
            Q = deque([(r, c)])
            area = 0
            perim = dict()
            while Q:
                r2, c2 = Q.popleft()
                if (r2, c2) in seen:
                    continue
                seen.add((r2, c2))
                area += 1
                for dr, dc in dirs:
                    rr = r2 + dr
                    cc = c2 + dc
                    if (
                        0 <= rr < rows
                        and 0 <= cc < cols
                        and region[rr][cc] == region[r2][c2]
                    ):
                        Q.append((rr, cc))
                    else:
                        if (dr, dc) not in perim:
                            perim[(dr, dc)] = set()
                        perim[(dr, dc)].add((r2, c2))

            sides = 0
            for _, vs in perim.items():
                seen_perim = set()
                for pr, pc in vs:
                    if (pr, pc) not in seen_perim:
                        sides += 1
                        Q = deque([(pr, pc)])
                        while Q:
                            r2, c2 = Q.popleft()
                            if (r2, c2) in seen_perim:
                                continue
                            seen_perim.add((r2, c2))
                            for dr, dc in dirs:
                                rr, cc = r2 + dr, c2 + dc
                                if (rr, cc) in vs:
                                    Q.append((rr, cc))
            ans += area * sides
    return ans


print(part1("input.txt"))
print(part2("input.txt"))
