from collections import deque

workflows, parts = open("input.txt").read().split("\n\n")
criteria = {"A": "A", "R": "R"}
rules = {}
for line in workflows.splitlines():
    name, ratings = line[:-1].split("{")
    ratings = ratings.replace(":", " and ").replace(",", " or ")
    rules[name] = ratings
    criteria[name] = name

ans = 0
for p in parts.splitlines():
    x, m, a, s = [int(el[2:]) for el in p[1:-1].split(",")]
    curr = "in"
    while curr not in "AR":
        curr = eval(rules[curr], criteria, locals())
    if curr == "A":
        ans += x + m + a + s

print(ans)


class Range:
    def __init__(self, name, range=None) -> None:
        self.name = name
        self.range = range

    def __lt__(self, other):
        return Range(self.name, range(1, other))

    def __gt__(self, other):
        return Range(self.name, range(other + 1, 4001))

    def __repr__(self):
        return f"name={self.name}, range={self.range}"


def split_range(a, b):
    sect = range(max(a.start, b.start), min(a.stop, b.stop))
    left = range(a.start, sect.start)
    right = range(sect.stop, a.stop)
    return left, sect, right


criteria = {"A": "A", "R": "R"}
for line in workflows.splitlines():
    name, _ = line[:-1].split("{")
    criteria[name] = name

rules = {}
for line in workflows.splitlines():
    name, ratings = line.split("{")
    x, m, a, s = Range("x"), Range("m"), Range("a"), Range("s")
    ratings = "{" + ",None:".join(ratings.rsplit(",", 1))
    rules[name] = eval(ratings, globals(), criteria)

q = deque()
q.append(("in", *[range(1, 4001) for _ in range(4)]))
ans = 0

while q:
    curr, x, m, a, s = q.popleft()
    if curr == "R":
        continue
    if curr == "A":
        ans += len(x) * len(a) * len(m) * len(s)
        continue
    for k, v in rules[curr].items():
        if k is None:
            q.append((v, x, m, a, s))
            continue
        (
            left,
            sect,
            right,
        ) = split_range(eval(k.name), k.range)
        assert not (left and right)
        exec(f"global {k.name}; {k.name} = sect")
        q.append((v, x, m, a, s))
        exec(f"global {k.name}; {k.name} = left or right")

print(ans)
