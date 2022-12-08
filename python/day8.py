#!/usr/bin/python

import numpy as np

def lmapi(*args, **kwargs):
    return list(map(int, *args, **kwargs))

def dist(this, ar):
    count = 0
    for other in ar:
        count += 1
        if other >= this:
            break
    return count

def solve(input_fname):
    lines = []
    with open(input_fname) as ifile:
        for line in ifile:
            lines.append(lmapi(line.strip()))
    ar = np.array(lines)

    width, height = ar.shape
    visible = 2*width + 2*(height-2)  # edge trees
    scenic = np.zeros_like(ar)
    for x in range(1,width-1):
        for y in range(1,height-1):
            this = ar[y][x]
            # slices of visible trees in each direction
            l = ar[y,:x]
            r = ar[y,x+1:]
            t = ar[:y,x]
            b = ar[y+1:,x]

            # [part 1]
            if min(map(max, (l, r, t, b))) < this:
                visible += 1

            # [part 2]
            dists = [dist(this, l[::-1]),
                     dist(this, r),
                     dist(this, t[::-1]),
                     dist(this, b)]
            scenic[y,x] = np.array(dists).prod()

    # return visible  # [part 1]
    return scenic.max()

if __name__ == "__main__":
    print(solve("../inputs/day8.in"))
