platform = open("input.txt", "r").read().strip()
platform = [list(line) for line in platform.split("\n")]


def move(platform):
    for row in platform:
        slot = 0
        for i, c in enumerate(row):
            if c == "#":
                slot = i + 1
            if c == "O":
                row[i] = "."
                row[slot] = "O"
                slot += 1


def transpose(platform):
    return [list(x) for x in zip(*platform)]


transposed_platform = transpose(platform)
move(transposed_platform)
new_platform = transpose(transposed_platform)

total_sum = sum(
    (len(new_platform) - i) * line.count("O") for i, line in enumerate(new_platform)
)

print(total_sum)


def spin_cycle(platform, cycles=1000000000):
    states = {}
    i = 0

    while i < cycles:
        joined = "\n".join("".join(row) for row in platform)
        if joined in states:
            cycle = i - states[joined]
            i += (cycles - i) // cycle * cycle
            if i == cycles:
                break

        states[joined] = i

        platform = transpose(platform)
        move(platform)
        platform = transpose(platform)

        move(platform)

        platform = platform[::-1]
        platform = transpose(platform)
        move(platform)
        platform = transpose(platform)
        platform = platform[::-1]

        platform = [row[::-1] for row in platform]
        move(platform)
        platform = [row[::-1] for row in platform]

        i += 1

    new_platform = transpose(platform)
    return new_platform


new_platform = spin_cycle(platform)
total_sum = sum(
    i + 1 for col in new_platform for i, c in enumerate(col[::-1]) if c == "O"
)
print(total_sum)
