@tuple
class Claw:
    ax: int
    ay: int
    bx: int
    by: int
    px: int
    py: int

@llvm
def calc(a: int, b: int) -> int:
    %cost_a = mul i64 %a, 3
    %total = add i64 %cost_a, %b
    ret i64 %total

def parse(s: str, higher: Optional[int] = 0) -> Tuple[int, int]:
    parts = s.split(",")
    x = "".join(c for c in parts[0] if c.isdigit())
    y = "".join(c for c in parts[1] if c.isdigit())
    x = higher + int(x)
    y = higher + int(y)
    return x, y

def solve(c: Claw, max_tries: int = 100) -> int:
    # ax * a + bx * b = px
    # ay * a + by * b = py
    @par(num_threads=max_tries // 100)
    for a in range(max_tries + 1):
        if c.bx != 0:
            b_x = (c.px - c.ax * a) / c.bx
        else:
            if c.ax * a != c.px:
                continue
            b_x = 0

        if b_x != int(b_x) or b_x < 0 or b_x > max_tries:
            continue
        b_x = int(b_x)

        if c.ay * a + c.by * b_x == c.py:
            return calc(a, b_x)
    return 0

def part1(file: str) -> int:
    with open(file) as f:
        config = f.read().strip()

    machines = []

    for cfg in config.split("\n\n"):
        lines = cfg.strip().split("\n")
        ax, ay = parse(lines[0].split(": ")[1])
        bx, by = parse(lines[1].split(": ")[1])
        px, py = parse(lines[2].split(": ")[1])
        machines.append(Claw(ax, ay, bx, by, px, py))

    ans = 0
    for m in machines:
        tokens = solve(m)
        ans += tokens
    return ans

def part2(file: str) -> int:
    with open(file) as f:
        config = f.read().strip()

    high = 10000000000000
    machines = []

    for cfg in config.split("\n\n"):
        lines = cfg.strip().split("\n")
        ax, ay = parse(lines[0].split(": ")[1])
        bx, by = parse(lines[1].split(": ")[1])
        px, py = parse(lines[2].split(": ")[1], high)
        machines.append(Claw(ax, ay, bx, by, px, py))

    ans = 0
    for m in machines:
        tokens = solve(m, high * 10)
        ans += tokens
    return ans

print(part1("input.txt"))

