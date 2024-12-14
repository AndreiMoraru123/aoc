from python import z3


@tuple
class Claw:
    ax: int
    ay: int
    bx: int
    by: int
    px: int
    py: int


def parse(s: str, higher: Optional[int] = 0) -> Tuple[int, int]:
    parts = s.split(",")
    x = "".join(c for c in parts[0] if c.isdigit())
    y = "".join(c for c in parts[1] if c.isdigit())
    x = higher + int(x)
    y = higher + int(y)
    return x, y


def solve(c: Claw) -> int:
    x1 = z3.Int("x1")
    x2 = z3.Int("x2")

    solver = z3.Solver()
    solver.add(x1 * c.ax + x2 * c.bx == c.px)
    solver.add(x1 * c.ay + x2 * c.by == c.py)

    if solver.check() == z3.sat:
        m = solver.model()
        ret = m.eval(3 * x1 + x2).as_long()
        return ret
    else:
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
        ans += solve(m)
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
        ans += solve(m)
    return ans


print(part1("input.txt"))
print(part2("input.txt"))
