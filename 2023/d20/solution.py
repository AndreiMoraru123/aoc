from pprint import pprint
from math import prod
from collections import defaultdict, deque

f = open("input.txt")
types = {}
conj_state = defaultdict(dict)
flip_state = defaultdict(bool)

for line in f:
    sender, receivers = line.strip().split(" -> ")
    receivers = receivers.split(", ")
    types[sender[1:]] = sender[0], receivers
    for receiver in receivers:
        conj_state[receiver][sender[1:]] = False

counts = defaultdict(int)
q = deque()

def send(s: str, r: str, state: bool) -> None:
    counts[state] += 1
    conj_state[r][s] = state
    q.append((r, state))


for _ in range(1000):
    send("button", "roadcaster", False)
    while q:
        x, state = q.popleft()
        if x not in types:
            continue
        match types[x]:
            case "b", receivers:
                for receiver in receivers:
                    send(x, receiver, state)
            case "%", receivers if not state:
                flip_state[x] = not flip_state[x]
                for receiver in receivers:
                    send(x, receiver, flip_state[x])
            case "&", receivers:
                pulse = not all(conj_state[x].values())
                for receiver in receivers:
                    send(x, receiver, pulse)

print(prod(counts.values()))

types = {}

conj_state = defaultdict(dict)
flip_state = defaultdict(bool)

f = open('toy_input.txt')
for line in f:
    sender, receivers = line.strip().split(' -> ')
    receivers = receivers.split(', ')
    types[sender[1:]] = sender[0], receivers
    for receiver in receivers:
        conj_state[receiver][sender[1:]] = False
    
def reset_states():
    for key in flip_state.keys():
        flip_state[key] = False
    for key, value in conj_state.items():
        for k in value.keys():
            conj_state[key][k] = False

min_button_presses = float('inf')
press_count = 0

while press_count < min_button_presses:

    reset_states()
    counts = defaultdict(int)
    q = deque()

    for _ in range(press_count + 1):
        send("button", "roadcaster", False)
        while q:
            x, state = q.popleft()
            if not x in types:
                if x == "rx" and not state:
                    min_button_presses += 1
                continue
            match types[x]:
                case "b", receivers:
                    for receiver in receivers:
                        send(x, receiver, state)
                case "%", receivers:
                    flip_state[x] = not flip_state[x]
                    for receiver in receivers:
                        send(x, receiver, flip_state[x])
                case "&", receivers:
                    pulse = not all(conj_state[x].values())
                    for receiver in receivers:
                        send(x, receiver, pulse)
        press_count += 1

print(min_button_presses)
