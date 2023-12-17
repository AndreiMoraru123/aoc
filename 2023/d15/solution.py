from collections import defaultdict

def hash(string: str) -> int:
    h = 0
    for c in string:
        c = ord(c)
        h += c
        h *= 17
        h %= 256
    return h

f = open('input.txt').read().strip()
answer = map(hash, f.split(','))
print(sum(answer))

hashmap = defaultdict(dict)

for sequence in f.split(','):
    if "=" in sequence:
        lens, focal_length = sequence.split("=")
        hashmap[hash(lens)][lens] = int(focal_length)
    elif "-" in sequence:
        lens = sequence[:-1]
        hashmap[hash(lens)].pop(lens, None)

answer = sum(
    (i + 1) * (j + 1) * focal_length
    for i, box in hashmap.items()
    for j, focal_length in enumerate(box.values())
)

print(answer)
