from itertools import product

@llvm
def eval(acc: int, num: int, opcode: int) -> int:
    %is_add = icmp eq i64 %opcode, 0
    %sum = add i64 %acc, %num
    %prod = mul i64 %acc, %num
    %result = select i1 %is_add, i64 %sum, i64 %prod
    ret i64 %result


def evalexpr(nums: List[int], ops: List[str]):
    result = nums[0]
    for i, op in enumerate(ops):
        opcode = 0 if op == "+" else 1
        result = eval(result, nums[i + 1], opcode)
    return result


def evalexpr2(nums: List[int], ops: List[str]):
    result = nums[0]
    for i, op in enumerate(ops):
        if op == "+":
            result += nums[i + 1]
        elif op == "*":
            result *= nums[i + 1]
        else:
            result = result * 10 ** len(str(nums[i + 1])) + nums[i + 1]
    return result


def genexpr(numbers: List[int], operators=("*", "+")):
    return product(operators, repeat=len(numbers) - 1)


def genexpr2(numbers: List[int], operators=("*", "+", "||")):
    return product(operators, repeat=len(numbers) - 1)


def part1(file: str) -> int:
    ans = 0
    with open(file) as f:
        lines = f.read().strip()
        for line in lines.split("\n"):
            total, nums = line.split(":")
            total = int(total)
            nums = [int(num) for num in nums.split()]
            for ops in genexpr(nums):
                if evalexpr(nums, ops) == total:
                    ans += total
                    break
    return ans


def part2(file: str) -> int:
    ans = 0
    with open(file) as f:
        lines = f.read().strip()
        for line in lines.split("\n"):
            total, nums = line.split(":")
            total = int(total)
            nums = [int(num) for num in nums.split()]
            for ops in genexpr2(nums):
                if evalexpr2(nums, ops) == total:
                    ans += total
                    break
    return ans


print(part1("input.txt"))
print(part2("input.txt"))
