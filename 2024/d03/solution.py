import re

@llvm
def mul(a: int, b: int) -> int:
    %res = mul i64 %a, %b
    ret i64 %res


def part1(file: str) -> int:
    ans = 0
    with open(file) as f:
        text = f.read().strip()
        pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
        matches = re.finditer(pattern, text)
        for pair in matches:
            x, y = list(map(int, pair.groups()))
            ans += mul(x,y)

    return ans


def part2(file: str) -> int:
    ans = 0
    with open(file) as f:
        text = f.read().strip()

    mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    do_pattern = r"do\(\)"
    dont_pattern = r"don\'t\(\)"

    instructions = []

    for pair in re.finditer(mul_pattern, text):
        x, y = list(map(int, pair.groups()))
        instructions.append((pair.start(), "mul", mul(x, y)))

    for pair in re.finditer(do_pattern, text):
        instructions.append((pair.start(), "do", 0))

    for pair in re.finditer(dont_pattern, text):
        instructions.append((pair.start(), "dont", 0))

    instructions.sort()

    state = [True]
    ans = 0

    for _, kind, value in instructions:
        if kind == "do":
            state[0] = True
        elif kind == "dont":
            state[0] = False
        elif kind == "mul" and state[0]:
            ans += value

    return ans


print(part1("input.txt"))
print(part2("input.txt"))
