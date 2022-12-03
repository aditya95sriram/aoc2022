#!/usr/bin/python3

import string

def solve(input_fname):
    lines = []
    with open(input_fname) as ifile:
        for line in ifile:
            lines.append(line.strip())
    priority = dict(zip(string.ascii_letters, range(1,53)))

    # [part 1]
    total = 0
    for sack in lines:
        left, right = sack[:len(sack)//2], sack[len(sack)//2:]
        common = set(left).intersection(set(right)).pop()
        total += priority[common]
    print(total)
    # return total  # [part 1]

    # [part 2]
    total = 0
    for i in range(0, len(lines), 3):
        s1, s2, s3 = lines[i:i+3]
        badge = set(s1).intersection(s2, s3).pop()
        total += priority[badge]
    return total

if __name__ == "__main__":
    print(solve("../inputs/day3.in"))
