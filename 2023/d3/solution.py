from typing import List, Callable

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

def process_adjacent_cells(matrix: List[List[str]], x: int, y: int, rule: Callable) -> List[str]:
    results = []
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(matrix) and 0 <= ny < len(matrix[0]):
            result = rule(matrix, nx, ny)
            if result is not None:
                results.append(result)
    return results

def is_adjacent(matrix: List[List[str]], x: int, y: int) -> bool:

    def is_symbol(char: str):
        return not char.isdigit() and char != '.'

    def check_symbol(m, i, j):
        return is_symbol(m[i][j])

    return any(process_adjacent_cells(matrix, x, y, check_symbol))

def get_adjacent_numbers(matrix: List[List[str]], x: int, y: int) -> List[int]:
    adj_numbers = []
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(matrix) and 0 <= ny < len(matrix[0]) and matrix[nx][ny].isdigit():
            start_ny = ny # trace back to the start of the number
            while start_ny > 0 and matrix[nx][start_ny-1].isdigit():
                start_ny -= 1
            if (nx, start_ny) not in adj_numbers: # avoid double counting
                adj_numbers.append((nx, start_ny))
    return [extract_number(matrix, x, y) for x, y in adj_numbers]


def extract_number(matrix: List[List[str]], x: int, y: int) -> int:
    number = ''
    while y < len(matrix[0]) and matrix[x][y].isdigit():
        number += matrix[x][y]
        y += 1
    return int(number)

def calculate_ratio(matrix: List[List[str]]) -> int:
    total_ratio = 0
    for i, row in enumerate(matrix):
        for j, char in enumerate(row):
            if char == '*':
                adj_numbers = get_adjacent_numbers(matrix, i, j)
                if len(adj_numbers) == 2:
                    total_ratio += adj_numbers[0] * adj_numbers[1]
    return total_ratio

def walk(matrix: List[List[str]]) -> int:
    s: int = 0
    for i, row in enumerate(matrix):
        j = 0  # start counting digits that form numbers
        while j < len(row):
            number = ''
            start_j = j
            if row[j].isdigit(): # the first digit
                while j < len(row) and row[j].isdigit(): # finding the whole number
                    number += row[j]
                    j += 1
                number = int(number)
                if any(is_adjacent(matrix, i, nj) for nj in range(start_j, j)):
                    s += number
            else:
                j += 1
    return s
                

with open('input.txt', 'r') as f:
    matrix = [list(line.strip()) for line in f]

total_sum = walk(matrix)
print(total_sum)

gear_ratio = calculate_ratio(matrix)
print(gear_ratio)
