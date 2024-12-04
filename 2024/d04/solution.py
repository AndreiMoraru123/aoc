def part1(file: str) -> int:
    ans = 0
    with open(file) as f:
        lines = f.read().strip().splitlines()

    rows = len(lines)
    cols = len(lines[0])
    for r in range(rows):
        for c in range(cols):
            if (
                c + 3 < cols
                and lines[r][c] == "X"
                and lines[r][c + 1] == "M"
                and lines[r][c + 2] == "A"
                and lines[r][c + 3] == "S"
            ):
                ans += 1
            if (
                r + 3 < rows
                and lines[r][c] == "X"
                and lines[r + 1][c] == "M"
                and lines[r + 2][c] == "A"
                and lines[r + 3][c] == "S"
            ):
                ans += 1
            if (
                r + 3 < rows
                and c + 3 < cols
                and lines[r][c] == "X"
                and lines[r + 1][c + 1] == "M"
                and lines[r + 2][c + 2] == "A"
                and lines[r + 3][c + 3] == "S"
            ):
                ans += 1
            if (
                r - 3 >= 0
                and c + 3 < cols
                and lines[r][c] == "X"
                and lines[r - 1][c + 1] == "M"
                and lines[r - 2][c + 2] == "A"
                and lines[r - 3][c + 3] == "S"
            ):
                ans += 1
            if (
                c + 3 < cols
                and lines[r][c] == "S"
                and lines[r][c + 1] == "A"
                and lines[r][c + 2] == "M"
                and lines[r][c + 3] == "X"
            ):
                ans += 1
            if (
                r + 3 < rows
                and lines[r][c] == "S"
                and lines[r + 1][c] == "A"
                and lines[r + 2][c] == "M"
                and lines[r + 3][c] == "X"
            ):
                ans += 1
            if (
                r + 3 < rows
                and c + 3 < cols
                and lines[r][c] == "S"
                and lines[r + 1][c + 1] == "A"
                and lines[r + 2][c + 2] == "M"
                and lines[r + 3][c + 3] == "X"
            ):
                ans += 1
            if (
                r - 3 >= 0
                and c + 3 < cols
                and lines[r][c] == "S"
                and lines[r - 1][c + 1] == "A"
                and lines[r - 2][c + 2] == "M"
                and lines[r - 3][c + 3] == "X"
            ):
                ans += 1
    return ans


def part2(file: str) -> int:
    ans = 0
    with open(file) as f:
        lines = f.read().strip().splitlines()

    rows = len(lines)
    cols = len(lines[0])
    for r in range(rows):
        for c in range(cols):
            if (
                r + 2 < rows
                and c + 2 < cols
                and lines[r][c] == "M"
                and lines[r + 1][c + 1] == "A"
                and lines[r + 2][c + 2] == "S"
                and lines[r + 2][c] == "M"
                and lines[r][c + 2] == "S"
            ):
                ans += 1
            if (
                r + 2 < rows
                and c + 2 < cols
                and lines[r][c] == "M"
                and lines[r + 1][c + 1] == "A"
                and lines[r + 2][c + 2] == "S"
                and lines[r + 2][c] == "S"
                and lines[r][c + 2] == "M"
            ):
                ans += 1
            if (
                r + 2 < rows
                and c + 2 < cols
                and lines[r][c] == "S"
                and lines[r + 1][c + 1] == "A"
                and lines[r + 2][c + 2] == "M"
                and lines[r + 2][c] == "M"
                and lines[r][c + 2] == "S"
            ):
                ans += 1
            if (
                r + 2 < rows
                and c + 2 < cols
                and lines[r][c] == "S"
                and lines[r + 1][c + 1] == "A"
                and lines[r + 2][c + 2] == "M"
                and lines[r + 2][c] == "S"
                and lines[r][c + 2] == "M"
            ):
                ans += 1
    return ans


print(part1("input.txt"))
print(part2("input.txt"))
