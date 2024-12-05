from collections import defaultdict, deque


def part1(file: str) -> int:
    ans = 0
    with open(file) as f:
        text = f.read().strip()
    edges, queries = text.split("\n\n")
    E = defaultdict(set)

    for line in edges.split("\n"):
        x, y = line.split("|")
        x, y = int(x), int(y)
        E[y].add(x)

    for query in queries.split("\n"):
        values = [int(x) for x in query.split(",")]
        ok = [True]
        for i, x in enumerate(values):
            for j, y in enumerate(values):
                if i < j and y in E[x]:
                    ok = [False]
        if ok[0]:
            ans += values[len(values) // 2]

    return ans


def part2(file: str) -> int:
    ans = 0
    with open(file) as f:
        text = f.read().strip()
    edges, queries = text.split("\n\n")
    E = defaultdict(set)
    ER = defaultdict(set)

    for line in edges.split("\n"):
        x, y = line.split("|")
        x, y = int(x), int(y)
        E[y].add(x)
        ER[x].add(y)

    for query in queries.split("\n"):
        values = [int(x) for x in query.split(",")]
        ok = [True]
        for i, x in enumerate(values):
            for j, y in enumerate(values):
                if i < j and y in E[x]:
                    ok = [False]
        if ok[0]:
            continue
        else:
            good = []
            Q = deque([])
            D = {v: len(E[v] & set(values)) for v in values}
            for v in values:
                if D[v] == 0:
                    Q.append(v)
            while Q:
                x = Q.popleft()
                good.append(x)
                for y in ER[x]:
                    if y in D:
                        D[y] -= 1
                        if D[y] == 0:
                            Q.append(y)
            ans += good[len(good) // 2]

    return ans


print(part1("input.txt"))
print(part2("input.txt"))
