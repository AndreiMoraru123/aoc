from collections import Counter

def part1(file: str) -> Int:
    left = List[int]()
    right = List[int]()

    with open(file) as f:
        # NOTE: left, right = zip(*(map(int, line.split()) for line in f)) # would work in Python
        for line in f:
            nums = [int(x) for x in line.split()]
            left.append(nums[0])
            right.append(nums[1])

    ans = 0
    left = sorted(left)
    right = sorted(right)

    @par
    for l, r in zip(left, right):
        ans += abs(l - r)
    return ans

def part2(file: str) -> Int:
    left = List[int]()
    right = Counter()

    with open(file) as f:
        for line in f:
            nums = [int(x) for x in line.split()]
            left.append(nums[0])
            right[nums[1]] +=1

    ans = 0
    left = sorted(left)

    @par
    for l in left:
        ans += l * right.get(l, 0)
    return ans


print(part1("input.txt"))
print(part2("input.txt"))
