from collections import Counter
from itertools import product


def rules(hand: str) -> int:
    occurences = [occurence for _, occurence in Counter(hand).most_common()]
    match occurences:
        case 5, *_:
            return 1
        case 4, *_:
            return 2
        case 3, 2, *_:
            return 3
        case 3, *_:
            return 4
        case 2, 2, *_:
            return 5
        case 2, *_:
            return 6
        case _:
            return 7


ORDER = "AKQJT98765432"
total_scores = []

JOKER_ORDER = "AKQT98765432J"
joker_total_scores = []

with open("input.txt", "r") as f:
    for line in f:
        hand, bid = line.split()
        rank = rules(hand)
        order = [ORDER.index(card) for card in hand]
        bid = int(bid)

        joker_order = [JOKER_ORDER.index(card) for card in hand]

        total_scores.append((rank, order, bid))

        for joker_substitutions in product(JOKER_ORDER[:-1], repeat=hand.count("J")):
            new_hand = rules(hand.replace("J", "") + "".join(joker_substitutions))
            rank = min(rank, new_hand)

        joker_total_scores.append((rank, joker_order, bid))

total_scores.sort(reverse=True)  # in case ranks are equal, order decides the sorting
joker_total_scores.sort(reverse=True)

total_sum = sum((rank + 1) * score[-1] for rank, score in enumerate(total_scores))
print(total_sum)

joker_total_sum = sum(
    (rank + 1) * score[-1] for rank, score in enumerate(joker_total_scores)
)
print(joker_total_sum)
