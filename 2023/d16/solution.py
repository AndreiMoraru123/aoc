from collections import deque


class SmartTuple(tuple):
    def __add__(self, other):
        return SmartTuple(x + y for x, y in zip(self, other))

directions = {
    "right": SmartTuple((0, 1)),
    "left": SmartTuple((0, -1)),
    "down": SmartTuple((1, 0)),
    "up": SmartTuple((-1, 0)),
}

def walk(contraption, start, dstart):
    q = deque([(SmartTuple(start), SmartTuple(dstart))])
    visited = set()
    while q:
        i, di = q.popleft()
        if i not in contraption or (i, di) in visited:
            continue
        visited.add((i, di))
        match contraption[i]:
            case "/":
                di = -di[1], -di[0]
                q.append((i + di, di))
            case "\\":
                di = di[1], di[0]
                q.append((i + di, di))
            case "|" if di[0] == 0:
                q.append((i + directions["up"], directions["up"]))
                q.append((i + directions["down"], directions["down"]))
            case "-" if di[1] == 0:
                q.append((i + directions["right"], directions["right"]))
                q.append((i + directions["left"], directions["left"]))
            case _:
                q.append((i + di, di))

    return len(set(i for i, _ in visited))


f = open('input.txt')
contraption = {(i, j): c for i, line in enumerate(f) for j, c in enumerate(line.strip())}
answer = walk(contraption, (0, 0), directions["right"])
print(answer)

f = open('input.txt')
lines = f.read().splitlines()
n, m = len(lines), len(lines[0])


ans = 0
for i in range(n):
    ans = max(ans, walk(contraption, (0, i), directions['down']))
    ans = max(ans, walk(contraption, (n - 1, i), directions['up']))
for i in range(n):
    ans = max(ans, walk(contraption, (i, 0), directions['right']))
    ans = max(ans, walk(contraption, (i, m - 1), directions['left']))

print(ans)
