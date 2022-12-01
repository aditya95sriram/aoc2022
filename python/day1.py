#!/usr/bin/python3

def solve(input_fname):
    lines = []
    elfs = [0]
    with open(input_fname) as ifile:
        for line in ifile:
            if line.strip():
                elfs[-1] += int(line.strip())
            else:
                elfs.append(0)
    return sum(sorted(elfs, reverse=True)[:3])

if __name__ == "__main__":
    print(solve("../inputs/day1.in"))