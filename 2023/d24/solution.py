from typing import NamedTuple, List


class Position(NamedTuple):
    x: int
    y: int
    z: int


class Velocity(NamedTuple):
    x: int
    y: int
    z: int


class Trajectory(NamedTuple):
    pos: Position
    vel: Velocity


lines = open("input.txt").read().splitlines()

trajectories: List[Trajectory] = []
for l in lines:
    pos, vel = l.split("@")
    coords = pos.split(", ")
    coords = [int(c) for c in coords]
    pos = Position(*coords)

    speeds = vel.split(", ")
    speeds = [int(s) for s in speeds]
    vel = Velocity(*speeds)
    trajectory = Trajectory(pos, vel)
    trajectories.append(trajectory)

least = 200000000000000
most = 400000000000000

ans = 0
for i in range(len(trajectories)):
    for j in range(i + 1, len(trajectories)):
        # Line equations:
        # x = x1 + t * (x2 - x1)
        # y = y1 + t * (y2 - y1)
        # where (x1, y1) and (x2, y2) are two points that form the line

        # x2 is x1 after one time unit and so on
        # since the trajectory is lines, two points at any time define the line
        x1 = trajectories[i].pos.x
        x2 = trajectories[i].pos.x + trajectories[i].vel.x
        x3 = trajectories[j].pos.x
        x4 = trajectories[j].pos.x + trajectories[j].vel.x

        y1 = trajectories[i].pos.y
        y2 = trajectories[i].pos.y + trajectories[i].vel.y
        y3 = trajectories[j].pos.y
        y4 = trajectories[j].pos.y + trajectories[j].vel.y

        # System of equations:
        # x1 + t * (x2 - x1) = x3 + u * (x4 - x3)
        # y1 + t * (y2 - y1) = y3 + u * (y4 - y3)

        # Rearange:
        # t * (x2 - x1) - u * (x4 - x3) = x3 - x1
        # t * (y2 - y1) - u * (y4 - y3) = y3 - y1

        # Matrix Form Ax = B:
        # [x2 - x1  -(x4 - x3)] * [t] = [x3 - x1]
        # [y2 - y1  -(y4 - y3)] * [u] = [y3 - y1]

        # Cramers rule:
        # The determinant represent the are of the intersection
        determinant = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
        if determinant != 0:  # if 0, the lines would be parallel
            # compute the intersection point
            px = (x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)
            px /= determinant
            py = (x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)
            py /= determinant

            valid = (px > x1) == (x2 > x1) and (px > x3) == (x4 > x3)
            if least < px < most and least < py < most and valid:
                ans += 1

print(ans)
