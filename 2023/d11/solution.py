from itertools import combinations

with open("input.txt") as f:
    image = [line.strip() for line in f]

no_galaxy_rows = {row for row, line in enumerate(image) if "#" not in line}
no_galaxy_cols = {
    col for col in range(len(image[0])) if "#" not in [line[col] for line in image]
}

galaxies = {
    (x, y)
    for x in range(len(image))
    for y in range(len(image[0]))
    if image[x][y] == "#"
}

total_distance = sum(
    abs(p[0] - q[0])
    + abs(p[1] - q[1])
    + len(no_galaxy_rows & set(range(min(p[0], q[0]), max(p[0], q[0]) + 1)))
    + len(no_galaxy_cols & set(range(min(p[1], q[1]), max(p[1], q[1]) + 1)))
    for p, q in combinations(galaxies, 2)
)
print(total_distance)

actual_total_distance = sum(
    abs(p[0] - q[0])
    + abs(p[1] - q[1])
    + 999999 * len(no_galaxy_rows & set(range(min(p[0], q[0]), max(p[0], q[0]) + 1)))
    + 999999 * len(no_galaxy_cols & set(range(min(p[1], q[1]), max(p[1], q[1]) + 1)))
    for p, q in combinations(galaxies, 2)
)

print(actual_total_distance)
