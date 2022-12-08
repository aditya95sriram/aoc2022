import re, os, sys
from functools import reduce
# from itertools import combinations as comb, permutations as perm, combinations_with_replacement as combr
from operator import itemgetter
from pprint import pprint
from math import *
from collections import defaultdict
import networkx as nx
import numpy as np
from itertools import pairwise
from dataclasses import dataclass, field

def dprint(d):
    pprint(dict(d))
def lmap(*args, **kwargs):
    return list(map(*args, **kwargs))
def lmapi(*args, **kwargs):
    return list(map(int, *args, **kwargs))
def enum(*args, **kwargs):
    return enumerate(*args, **kwargs)

def dist(this, ar, rev=False):
    count = 0
    if rev: ar = ar[::-1]
    # print("dist for", ar)
    for other in ar:
        if other < this:
            # print("saw", other)
            count += 1
        else:
            # print("blocked by", other)
            count += 1
            break
    return count

def solve(input_fname):
    lines = []
    with open(input_fname) as ifile:
        def ri(): 
            return int(ifile.readline().strip())
        def ris(): 
            return list(map(int, ifile.readline().strip().split()))
        for line in ifile:
            lines.append(lmapi(line.strip()))
    ar = np.array(lines)

    width, height = ar.shape
    visible = 2*width + 2*(height-2)  # edge trees
    print(width, height, visible)
    print(ar)
    scenic = np.zeros_like(ar)
    for x in range(1,width-1):
        for y in range(1,height-1):
            this = ar[y][x]
            left = ar[y,:x]
            right = ar[y,x+1:]
            top = ar[:y,x]
            bot = ar[y+1:,x]
            # [part 1]
            if min(left.max(), right.max(), top.max(), bot.max()) < this:
                visible += 1
            
            dl = [dist(this, left,True),
                  dist(this, right),
                  dist(this, top,True),
                  dist(this, bot)]
            # print("dists for", x, y, dl)
            scenic[y,x] = np.array(dl).prod()
            # break

            # print("vis", x, y, this_tree)
    print(scenic)
    # return visible  # [part 1]
    return scenic.max()







if __name__ == "__main__":
    print(solve("../inputs/day8.in"))
