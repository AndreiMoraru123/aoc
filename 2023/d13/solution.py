from typing import List

patterns = open("input.txt").read().split("\n\n")


def find(pattern: List[str]) -> int:
    for i in range(1, len(pattern)):
        if all(a == b for a, b in zip(pattern[:i][::-1], pattern[i:])):
            return i
    return 0


def find_smudge(pattern: List[str]) -> int:
    for i in range(1, len(pattern)):
        if (
            sum(
                ax != bx
                for a, b in zip(pattern[:i][::-1], pattern[i:])
                for ax, bx in zip(a, b)
            )
            == 1
        ):
            return i
    return 0


ans = 0
ans_smudge = 0
for pattern in patterns:
    pattern = pattern.splitlines()
    if h := find(pattern):
        ans += 100 * h
    if v := find(list(zip(*pattern))):
        ans += v
    if hs := find_smudge(pattern):
        ans_smudge += 100 * hs
    if vs := find_smudge(list(zip(*pattern))):
        ans_smudge += vs

print(ans)
print(ans_smudge)
