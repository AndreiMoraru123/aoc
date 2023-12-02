from typing import Dict

total_sum: int = 0

digits: Dict[str, str] = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def get_number(word: str, affix: str) -> str:
    for i in range(len(word)):
        if affix == "suffix":
            root = word[i:]
        elif affix == "prefix":
            root = word[: i + 1]
        else:
            raise ValueError("not supposed to be here")
        if root in digits:
            return digits[root]
    return ""


def walk(line: str, order: str) -> str:
    line_sum = ""
    word = ""
    for char in line:
        if char.isnumeric():
            line_sum += char
            break
        else:
            if order == "ordinary":
                word += char
                num = get_number(word, "suffix")
            elif order == "reversed":
                word = char + word
                num = get_number(word, "prefix")
            else:
                raise ValueError("not supposed to be here")
            if num:
                line_sum += num
                break
    return line_sum


with open("input.txt", "r") as f:
    for line in f:
        line = line.strip()
        ordinary_line_sum = walk(line, "ordinary")
        reversed_line_sum = walk(line, "reversed")
        line_sum = ordinary_line_sum + reversed_line_sum
        total_sum += int(line_sum)

print(total_sum)
