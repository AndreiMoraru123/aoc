from collections import deque


def part1(file: str) -> int:
    ans = 0
    with open(file) as f:
        disk = f.read().strip()

    A = deque([])
    space = deque([])
    pos = 0
    fid = 0
    final = []
    for i, c in enumerate(disk):
        if i % 2 == 0:
            for _ in range(int(c)):
                A.append((pos, fid))
                final.append(fid)
                pos += 1
            fid += 1
        else:
            for _ in range(int(c)):
                space.append(pos)
                final.append(-1)
                pos += 1

    size = len(A)
    while A[-1][0] > space[0]:
        assert final[space[0]] == -1
        final[space[0]] = A[-1][1]
        A.pop()
        space.popleft()

    final = final[:size]
    for i, c in enumerate(final):
        if c != -1:
            ans += i * c
        else:
            break

    return ans


def part2(file: str) -> int:
    ans = 0
    with open(file) as f:
        disk = f.read().strip()

    A = []
    space = []
    pos = 0
    fid = 0
    final = []
    for i, c in enumerate(disk):
        if i % 2 == 0:
            A.append((pos, int(c), fid))
            for _ in range(int(c)):
                final.append(fid)
                pos += 1
            fid += 1
        else:
            space.append((pos, (int(c))))
            for _ in range(int(c)):
                final.append(-1)
                pos += 1

    for pos, sz, file_id in reversed(A):
        for i, (space_pos, space_sz) in enumerate(space):
            if space_pos < pos and sz <= space_sz:
                for j in range(sz):
                    assert final[pos + j] == file_id, f"{final[pos+j]=}"
                    final[pos + j] = -1
                    final[space_pos + j] = file_id
                space[i] = (space_pos + sz, space_sz - sz)
                break

    for i, c in enumerate(final):
        if c != -1:
            ans += i * c

    return ans


print(part1("input.txt"))
print(part2("input.txt"))
