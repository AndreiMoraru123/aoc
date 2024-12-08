from collections import defaultdict


@llvm
@pure
def dist(r: int, c: int, rx: int, cx: int) -> int:
    declare i64 @llvm.abs.i64(i64, i1)
    %dr = sub i64 %r, %rx
    %dc = sub i64 %c, %cx
    %abs_dr = call i64 @llvm.abs.i64(i64 %dr, i1 true)
    %abs_dc = call i64 @llvm.abs.i64(i64 %dc, i1 true)
    %d = add i64 %abs_dr, %abs_dc
    ret i64 %d

@llvm
@pure
def collinear(r: int, c: int, rx: int, cx: int, ry: int, cy: int) -> bool:
    %drx = sub i64 %r, %rx
    %dcx = sub i64 %c, %cx
    %dry = sub i64 %r, %ry
    %dcy = sub i64 %c, %cy

    %tx = mul i64 %drx, %dcy
    %ty = mul i64 %dcx, %dry
    %eq = icmp eq i64 %tx, %ty
    %col = zext i1 %eq to i8
    ret i8 %col


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
                            d1 = dist(r, c, r1, c1)
                            d2 = dist(r, c, r2, c2)

                            if (
                                collinear(r, c, r1, c1, r2, c2)
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
                            if (
                                collinear(r, c, r1, c1, r2, c2)
                                and 0 <= r < rows
                                and 0 <= c < cols
                            ):
                                a.add((r, c))

    ans = len(a)
    return ans


print(part1("input.txt"))
print(part2("input.txt"))
