def make_fs(disk: str) -> List[int]:
    fs = []
    id = 0
    for i, x in enumerate(disk):
        x = int(x)
        if i % 2 == 0:
            fs += [id] * x
            id += 1
        else:
            fs += [-1] * x
    return fs


def make_fs2(disk: str, loc: Array[int], size: Array[int]) -> List[int]:
    fs = []
    id = 0
    for i, x in enumerate(disk):
        x = int(x)
        if i % 2 == 0:
            loc[id] = len(fs)
            size[id] = x
            fs += [id] * x
            id += 1
        else:
            fs += [-1] * x
    return fs


def move(arr: List[int]) -> List[int]:
    first_free = 0
    while arr[first_free] != -1:
        first_free += 1
    i = len(arr) - 1
    while arr[i] == -1:
        i -= 1
    while i > first_free:
        arr[first_free] = arr[i]
        arr[i] = -1
        while arr[i] == -1:
            i -= 1
        while arr[first_free] != -1:
            first_free += 1
    return arr


def move2(arr: List[int], loc: Array[int], size: Array[int]) -> List[int]:
    big = 0
    while size[big] > 0:
        big += 1
    big -= 1

    for mv in range(big + 1, 0, -1):
        free_space = 0
        first_free = 0
        while first_free < loc[mv] and free_space < size[mv]:
            first_free = first_free + free_space
            free_space = 0
            while arr[first_free] != -1:
                first_free += 1
            while (
                first_free + free_space < len(arr)
                and arr[first_free + free_space] == -1
            ):
                free_space += 1

        if first_free >= loc[mv]:
            mv -= 1
            continue

        for idx in range(first_free, first_free + size[mv]):
            arr[idx] = mv
        for idx in range(loc[mv], loc[mv] + size[mv]):
            arr[idx] = -1
        mv -= 1

    return arr


def checksum(arr: List[int]) -> int:
    ans = 0
    for i, x in enumerate(arr):
        if x != -1:
            ans += i * x
    return ans


def part1(file: str) -> int:
    with open(file) as f:
        disk = f.read().strip()
    fs = make_fs(disk)
    fs = move(fs)
    ans = checksum(fs)
    return ans


def part2(file: str) -> int:
    with open(file) as f:
        disk = f.read().strip()
    size = __array__[int](10000)
    loc = __array__[int](10000)
    fs = make_fs2(disk, loc, size)
    fs = move2(fs, loc, size)
    ans = checksum(fs)
    return ans


print(part1("input.txt"))
print(part2("input.txt"))
