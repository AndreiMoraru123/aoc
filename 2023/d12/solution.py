from functools import cache
from itertools import combinations

@cache
def dp(chars, nums, *, curr=None):
    if len(nums) == 0 and curr is None:
        return "#" not in chars

    match chars[:1], curr:
        case "", None | 0:
            return len(nums) == 0
        case "", _:
            return 0

        case "?", None:
            return dp(chars[1:], nums) + dp(chars, nums[1:], curr=nums[0])
        case "?", 0:
            return dp(chars[1:], nums)
        case "?", _:
            return dp(chars[1:], nums, curr=curr - 1)

        case "#", None:
            return dp(chars, nums[1:], curr=nums[0])
        case "#", 0:
            return 0
        case "#", _:
            return dp(chars[1:], nums, curr=curr - 1)

        case ".", None | 0:
            return dp(chars[1:], nums)
        case ".", _:
            return 0


f  = open('input.txt')
ans = 0
ans_five = 0
for line in f:
    springs, counts = line.split()
    nums = [int(num) for num in counts.split(',')]
    questions = [i for i, char in enumerate(springs) if char == '?']
    
    for comb in combinations(questions, sum(nums) - springs.count('#')):
        arrangement = "".join('#' if i in comb else char for i, char in enumerate(springs))
        lst = [len(a) for a in arrangement.replace("?", ".").split(".") if a]
        if nums == lst:
            ans += 1

    springs = "?".join([springs] * 5)
    nums = tuple(int(x) for x in counts.split(",")) * 5
    ans_five += dp(springs, nums)
        
print(ans)
print(ans_five)
