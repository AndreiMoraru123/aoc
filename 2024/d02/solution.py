@llvm
def sub(a: int, b: int) -> int:
    %res = sub i64 %a, %b
    ret i64 %res

def part1(file: str) -> int:
    ans = 0
    with open(file) as f:
        lines = f.read().strip().split("\n")
        @par
        for line in lines:
            nums = [int(x) for x in line.split()]
            order = nums == sorted(nums) or nums == sorted(nums, reverse=True)
            ok = True
            for i in range(len(nums) - 1):
                diff = abs(sub(nums[i], nums[i + 1]))
                if not 1 <= diff <= 3:
                    ok = False
            if order and ok:
                ans += 1
    return ans


def part2(file: str) -> int:
    ans = 0
    with open(file) as f:
        lines = f.read().strip().split("\n")
        @par
        for line in lines:
            nums0 = [int(x) for x in line.split()]
            good = False
            for j in range(len(nums0)):
                nums = nums0[:j] + nums0[j + 1 :]
                order = nums == sorted(nums) or nums == sorted(nums, reverse=True)
                ok = True
                for i in range(len(nums) - 1):
                    diff = abs(sub(nums[i], nums[i + 1]))
                    if not 1 <= diff <= 3:
                        ok = False
                if order and ok:
                    good = True
            if good:
                ans += 1
    return ans


print(part1("input.txt"))
print(part2("input.txt"))
