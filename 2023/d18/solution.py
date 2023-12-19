class SmartTuple(tuple):
    def __add__(self, other):
        return SmartTuple(x + y for x, y in zip(self, other))
    def __mul__(self, other):
        return SmartTuple(x * other for x in self)

directions = {
    "R": SmartTuple((0, 1)),
    "L": SmartTuple((0, -1)),
    "D": SmartTuple((1, 0)),
    "U": SmartTuple((-1, 0)),
}


vertices = [SmartTuple((0, 0))]
perimeter = 0
f = open('input.txt')
for line in f:
    dir, num, _ = line.split()
    num = int(num)
    vertices.append(vertices[-1] + directions[dir] * num)
    perimeter += num

xs, ys = zip(*vertices)
shoelace = sum(a * b for a, b in zip(xs, ys[1:])) - sum(a * b for a, b in zip(ys, xs[1:]))
area = abs(shoelace) // 2
fill = area + perimeter // 2 + 1
print(fill)


vertices = [SmartTuple((0, 0))]
perimeter = 0
f = open('input.txt')
for line in f:
    _, _, hex = line.split()
    dir = "RDLU"[int(hex[-2])]
    num = int(hex[2:-2], 16)
    vertices.append(vertices[-1] + directions[dir] * num)
    perimeter += num

xs, ys = zip(*vertices)
shoelace = sum(a * b for a, b in zip(xs, ys[1:])) - sum(a * b for a, b in zip(ys, xs[1:]))
area = abs(shoelace) // 2
fill = area + perimeter // 2 + 1
print(fill)
