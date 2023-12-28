from typing import NamedTuple, Set, TypeAlias
from itertools import zip_longest


class Position(NamedTuple):
    x: int
    y: int
    z: int


Brick: TypeAlias = Set[Position]


def draw(begin: Position, end: Position) -> Brick:
    span = zip_longest(
        range(begin.x, end.x + 1), range(begin.y, end.y + 1), range(begin.z, end.z + 1)
    )
    positions = [Position(x or begin.x, y or begin.y, z or begin.z) for x, y, z in span]
    return set(positions)


def fall(tiles: Set[Brick], brick: Brick) -> Brick:
    while True:
        down = {Position(p.x, p.y, p.z - 1) for p in brick}
        if any(p.z == 0 for p in down) or down & tiles:
            return brick
        brick = down


f = open("input.txt")
bricks = []
tiles = set()
for line in f:
    begin, end = line.split("~")
    start_coords = begin.split(",")
    start_coords = [int(c) for c in start_coords]
    start_position = Position(*start_coords)

    end_coords = end.split(",")
    end_coords = [int(c) for c in end_coords]
    end_position = Position(*end_coords)
    brick = draw(start_position, end_position)
    bricks.append(brick)
    tiles.update(brick)

bricks.sort(key=lambda b: min(p.z for p in b))
for i, brick in enumerate(bricks):
    tiles -= brick
    bricks[i] = fall(tiles, brick)
    tiles.update(bricks[i])

ans = 0

for brick in bricks:
    without = tiles - brick
    for other in bricks:
        if other == brick:
            continue
        without -= other
        if fall(without, other) != other:
            break
        without.update(other)
    else:
        ans += 1

print(ans)


ans = 0

for brick in bricks:
    without = tiles - brick
    for other in bricks:
        if other == brick:
            continue
        without -= other
        if fall(without, other) != other:
            ans += 1
        else:
            without.update(other)

print(ans)
