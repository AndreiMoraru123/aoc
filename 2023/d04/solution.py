from collections import deque
from functools import reduce
from typing import List, Dict, Set


def build_number(sequence: str) -> List[int]:
    return [int(num) for num in sequence.split() if num.isnumeric()]


cards_worth: Dict[int, int] = {}
scratch_cards: Dict[int, Dict[str, Set[int]]] = {}

with open("input.txt", "r") as f:
    for line in f:
        winning_cards, given_numbers = line.strip().split("|")
        card_info, winning_numbers = winning_cards.strip().split(":")
        card_number = build_number(card_info).pop()

        winning_numbers_list = build_number(winning_numbers)
        given_numbers_list = build_number(given_numbers)

        matches = [n for n in given_numbers_list if n in winning_numbers_list]
        if matches:
            cards_worth[card_number] = reduce(
                lambda total, _: total * 2, range(len(matches) - 1), 1
            )
        else:
            cards_worth[card_number] = 0

        scratch_cards[card_number] = {
            "winning": set(winning_numbers_list),
            "given": set(given_numbers_list),
        }

total_points = sum(cards_worth.values())
print(total_points)

total_scratch_cards = 0
card_queue = deque(scratch_cards.items())

while card_queue:
    card_number, card_data = card_queue.popleft()
    total_scratch_cards += 1

    number_of_matches = len(card_data["given"] & card_data["winning"])
    for i in range(1, number_of_matches + 1):
        next_card_number = card_number + i
        if next_card_number in scratch_cards:
            card_queue.append((next_card_number, scratch_cards[next_card_number]))

print(total_scratch_cards)
