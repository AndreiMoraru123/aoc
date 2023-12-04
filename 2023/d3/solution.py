from typing import List, Tuple

directions = [
    (0, 1),  # right
    (0, -1),  # left
    (1, 0),  # up
    (-1, 0),  # down
    (1, -1),  # diagonal up left
    (-1, 1),  # diagonal down right
    (-1, -1),  # diagonal down left
    (1, 1),  # diagonal up right
]


def is_symbol(char: str) -> bool:
    return not char.isdigit() and char != "."


def is_gear(char: str) -> bool:
    return char == "*"


def extract_number(matrix: List[List[str]], x: int, y: int) -> int:
    number = ""
    while (
        y < len(matrix[0]) and matrix[x][y].isdigit()
    ):  # start constructing a number on a row
        number += matrix[x][y]
        y += 1
    return int(number)


def get_adjacent_numbers(matrix: List[List[str]], x: int, y: int) -> List[int]:
    adj_numbers = []
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if (
            0 <= nx < len(matrix)
            and 0 <= ny < len(matrix[0])
            and matrix[nx][ny].isdigit()
        ):
            start_ny = ny  # trace back to the start of the number
            while (
                start_ny > 0 and matrix[nx][start_ny - 1].isdigit()
            ):  # if the previous char is a digit, I'm not at the beginning of the number
                start_ny -= 1
            if (nx, start_ny) not in adj_numbers:  # avoid double counting
                adj_numbers.append((nx, start_ny))

    return [extract_number(matrix, x, y) for x, y in adj_numbers]


def walk(matrix: List[List[str]]) -> Tuple[int, int]:
    total_ratio = 0
    total_sum = 0
    for i, row in enumerate(matrix):
        for j, char in enumerate(row):
            if is_symbol(char):
                part_numbers = get_adjacent_numbers(matrix, i, j)
                total_sum += sum(part_numbers)
            if is_gear(char):
                adj_numbers = get_adjacent_numbers(matrix, i, j)
                if len(adj_numbers) == 2:
                    total_ratio += adj_numbers[0] * adj_numbers[1]
    return total_sum, total_ratio


with open("input.txt", "r") as f:
    matrix = [list(line.strip()) for line in f]

part_numbers_sum, gear_ratio = walk(matrix)
print(part_numbers_sum)
print(gear_ratio)
