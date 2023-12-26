from math import prod, lcm
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
rec = {}
origin = {}
inv = defaultdict(list)

conj_state = defaultdict(dict)
flip_state = defaultdict(bool)

f = open("input.txt")
for line in f:
    sender, receivers = line.strip().split(" -> ")
    receivers = receivers.split(", ")
    types[sender[1:]] = sender[0], receivers
    rec[sender] = receivers
    for receiver in receivers:
        conj_state[receiver][sender[1:]] = False


for sender, receivers in types.items():
    for receiver in receivers[1]:
        if types[sender][0] == "&":
            if receiver not in origin:
                origin[receiver] = {}
            origin[receiver][sender] = False
        inv[receiver].append(sender)

senders = inv[inv["rx"][0]]

q = deque()
prev = defaultdict(int)
lcm_counts = defaultdict(int)
cycles = []
on = set()
c = 0

while len(cycles) < len(senders):
    c += 1
    send("button", "roadcaster", False)
    while q:
        x, state = q.popleft()
        if state == False:
            # lcm_counts == 2 means state has been set to False 2 times => a full cycle has occured
            if x in prev and lcm_counts[x] == 2 and x in senders:
                cycles.append(c - prev[x])
            prev[x] = c
            lcm_counts[x] += 1
        if len(cycles) == len(senders):
            print(lcm(*cycles))
            break
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
