#!/usr/bin/python3

def lmapi(*args, **kwargs):
    return list(map(int, *args, **kwargs))

def solve(input_fname):
    ranges = []
    with open(input_fname) as ifile:
        for line in ifile:
            r1, r2 = line.strip().split(",")
            ranges.append((lmapi(r1.split("-")), lmapi(r2.split("-"))))

    count = 0
    for (a,b), (x,y) in ranges:
        interval1 = set(range(a,b+1))
        interval2 = set(range(x,y+1))
        # [part 1] check complete containment
        # cumulative = interval1 | interval2
        # if cumulative == interval1 or cumulative == interval2:
            # count += 1

        # [part 2] check for any overlap
        if interval1.intersection(interval2):
            count += 1
    return count

if __name__ == "__main__":
    print(solve("../inputs/day4.in"))
