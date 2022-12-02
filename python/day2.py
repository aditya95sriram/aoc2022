#!/usr/bin/python3

def solve(input_fname):
    lines = []
    with open(input_fname) as ifile:
        for line in ifile:
            lines.append(line.strip())
    
    win = dict(zip("ABC", "YZX"))
    draw = dict(zip("ABC", "XYZ"))
    loss = dict(zip("ABC", "ZXY"))
    scores = dict(zip("XYZ", (1,2,3)))

    # [part 1]
    total = 0
    for round in lines:
        op, me = round.split()
        total += scores[me]
        if me == draw[op]: total += 3
        elif me == win[op]: total += 6
    # return total  # [part 1]
    
    # [part 2]
    total = 0
    for round in lines:
        op, me = round.split()
        if me == "X":  # need to lose
            total += scores[loss[op]]
        elif me == "Y":  # need to draw
            total += scores[draw[op]] + 3
        else:  # need to win
            total += scores[win[op]] + 6
    return total  # [part 2]

if __name__ == "__main__":
    print(solve("../inputs/day2.in"))
