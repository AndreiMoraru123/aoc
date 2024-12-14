@tuple
class Pos:
    x: int
    y: int


@tuple
class Vel:
    x: int
    y: int


def move(pos: List[Pos], vel: List[Vel], n: int = 7, m: int = 11) -> List[Pos]:
    new_pos = []
    for p, v in zip(pos, vel):
        x = (p.x + v.x + n) % n
        y = (p.y + v.y + m) % m
        new_pos.append(Pos(x, y))
    return new_pos


def draw(pos: List[Pos], iteration: int, n: int, m: int, file: str = "output.txt"):
    grid = [["." for _ in range(n)] for _ in range(m)]
    for p in pos:
        grid[p.y][p.x] = "#"

    with open(file, "a") as f:
        f.write(f"Iteration {iteration}\n\n")
        for row in grid:
            f.write("".join(row) + "\n")
        f.write("\n")


def count(pos: List[Pos], n: int = 7, m: int = 11) -> int:
    q1 = q2 = q3 = q4 = 0
    for p in pos:
        if p.x == n // 2 or p.y == m // 2:
            continue
        if p.x < n // 2 and p.y < m // 2:
            q1 += 1
        elif p.x >= n // 2 and p.y < m // 2:
            q2 += 1
        elif p.x < n // 2 and p.y >= m // 2:
            q3 += 1
        elif p.x >= n // 2 and p.y >= m // 2:
            q4 += 1
    return q1 * q2 * q3 * q4


def create(file: str) -> Tuple[List[Pos], List[Vel]]:
    with open(file) as f:
        lines = f.read().strip().split("\n")

    pos = []
    vel = []
    for line in lines:
        a, b = line.split(" ")
        pc = a.split("=")[1].split(",")
        vc = b.split("=")[1].split(",")

        pos.append(Pos(int(pc[0]), int(pc[1])))
        vel.append(Vel(int(vc[0]), int(vc[1])))

    return pos, vel


def part1(file: str) -> int:
    pos, vel = create(file)
    for _ in range(100):
        pos = move(pos, vel, 101, 103)

    ans = count(pos, 101, 103)
    return ans


def part2(file: str) -> int:
    pos, vel = create(file)
    with open("output.txt", "w") as f:
        f.write("")

    for i in range(10**4):
        pos = move(pos, vel, 101, 103)
        draw(pos, i + 1, 101, 103)
        if i == 6515:  # check visually
            return i + 1

    return 0


print(part1("input.txt"))
print(part2("input.txt"))
