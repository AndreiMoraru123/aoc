def solve(file: str, iterations: int) -> int:
    with open(file) as f:
        arr = [int(x) for x in f.read().strip().split()]

    seen: Dict[Tuple[int, int], int] = {}

    def steps(x: int, t: int):
        if (x, t) in seen:
            return seen[(x, t)]
        if t == 0:
            ret = 1
        elif x == 0:
            ret = steps(1, t - 1)
        elif len(str(x)) % 2 == 0:
            s = str(x)
            left = s[: len(s) // 2]
            right = s[len(s) // 2 :]
            left, right = int(left), int(right)
            ret = steps(left, t - 1) + steps(right, t - 1)
        else:
            ret = steps(x * 2024, t - 1)

        seen[(x, t)] = ret
        return ret

    return sum(steps(x, iterations) for x in arr)


def part1(file: str) -> int:
    return solve(file, 25)


def part2(file: str) -> int:
    return solve(file, 75)


print(part1("input.txt"))
print(part2("input.txt"))
