import operator
from typing import Dict, Tuple
from functools import reduce

rules: Dict[str, int] = {
    'blue': 14,
    'green': 13,
    'red': 12,
}

def build_number(sequence: str) -> str:
    return ''.join([char for char in sequence if char.isnumeric()])

def validate(color: str, draw: str) -> bool:
    if color in draw:
        complete_number = build_number(draw)
        return int(complete_number) <= rules[color]
    return True

def process_game_line(line: str) -> Tuple[str, bool, int]:
    game_id, cubes_info = line.strip().split(':')
    nr = build_number(game_id)
    min_cubes = {color: 0 for color in rules}
    sets = cubes_info.split(';')

    for s in sets:
        for draw in s.split(','):
            for color in rules:
                if color in draw:
                    num_cubes = int(build_number(draw))
                    min_cubes[color] = max(min_cubes[color], num_cubes)
    power = reduce(operator.mul, (min_cubes[color] for color in rules))
    is_valid_game = all(validate(color, draw) for s in sets for color in rules for draw in s.split(','))
    return nr, is_valid_game, power

OK_GAME: Dict[str, bool] = {}

with open('input.txt', 'r') as f:
    min_viable_game_line = 0
    for line in f:
        game_number, is_valid, power = process_game_line(line)
        OK_GAME[game_number] = is_valid
        min_viable_game_line += power

print(sum(int(key) for key, value in OK_GAME.items() if value))
print(min_viable_game_line)
        
