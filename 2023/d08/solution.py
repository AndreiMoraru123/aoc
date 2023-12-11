import math
from itertools import cycle

with open('input.txt') as f:
    instructions, network = f.read().split('\n\n')
    network = [x.split(" = ") for x in network.splitlines()]
    
    mapping = {a: b[1:-1].split(', ') for a, b in network}

    curr = 'AAA'
    
    for i, dir in enumerate(cycle(instructions), start=1):
        curr = mapping[curr][dir == 'R']
        if curr == 'ZZZ':
            print(i)
            break

    possibilities = []

    for curr in mapping:
        if not curr.endswith('A'):
            continue
        for i, (idx, dir) in enumerate(cycle(enumerate(instructions)), start=1):
            prev, curr = curr, mapping[curr][dir == 'R']
            if prev.endswith('Z'):
                possibilities.append(i-1)
                break
    print(math.lcm(*possibilities))

