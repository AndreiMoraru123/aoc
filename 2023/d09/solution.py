from typing import List

def get_differences(line: List[int]) -> List[int]:
    return [end - start for start, end in zip(line, line[1:])]

def find_last_element(line: List[int]) -> int:
    if not(any(line)):
        return 0
    diffs = get_differences(line)
    return line[-1] + find_last_element(diffs)

def find_first_element(line: List[int]) -> int:
    if not(any(line)):
        return 0
    diffs = get_differences(line)
    return line[0] - find_first_element(diffs)


lines = open("input.txt").read().strip().split("\n")
lines = [[int(i) for i in line.split()] for line in lines]

print(sum([find_last_element(line) for line in lines]))
print(sum([find_first_element(line) for line in lines]))

