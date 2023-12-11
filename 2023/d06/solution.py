from math import sqrt
from functools import reduce
from typing import List


def build_numbers(sequence: str) -> List[int]:
    return [int(num) for num in sequence.split() if num.isnumeric()]


def compute_score(hold_time: int, record_time: int) -> int:
    return hold_time * (record_time - hold_time)


def find_max_range(race_time: int, record_distance: int) -> int:
    # hold_time * (record_time - hold_time) = -hold_time**2 + hold_time * record_time
    a = 1
    b = -race_time
    c = record_distance

    discriminant = b**2 - 4 * a * c

    if discriminant < 0:
        return 0  # no real solutions

    # roots where the distance equals the record
    root1 = (-b + sqrt(discriminant)) / (2 * a)
    root2 = (-b - sqrt(discriminant)) / (2 * a)

    # but the actual parabola is downwards, so the bigger values are above, i.e. in between the roots

    lower_bound = int(root1) + 1 if root1 < root2 else int(root2) + 1
    upper_bound = int(root2) if root1 < root2 else int(root1)

    return max(0, upper_bound - lower_bound + 1)


with open("input.txt", "r") as f:
    time, distance = f.read().splitlines()
    times = build_numbers(time)
    distances = build_numbers(distance)


records = dict(map(lambda i, j: (i, j), times, distances))
possible_scores = {}

for time in times:
    possible_scores[time] = 0
    for ms in range(time + 1):
        distance_reached = compute_score(ms, time)
        if distance_reached > records[time]:
            possible_scores[time] += 1

prod = reduce(lambda a, b: a * b, possible_scores.values())
print(prod)

actual_time = "".join([str(t) for t in times])
actual_distance = "".join([str(t) for t in distances])

actual_time = int(actual_time)
actual_distance = int(actual_distance)

number_of_ways = find_max_range(actual_time, actual_distance)
print(number_of_ways)
