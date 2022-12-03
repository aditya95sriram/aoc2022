import re, os, sys
from functools import reduce
from itertools import combinations as comb, permutations as perm, combinations_with_replacement as combr
from operator import itemgetter
from pprint import pprint
from math import *
from collections import defaultdict
import networkx as nx
import numpy as np

import string

def dprint(d):
    pprint(dict(d))
def lmap(*args, **kwargs):
    return list(map(*args, **kwargs))
def lmapi(*args, **kwargs):
    return list(map(int, *args, **kwargs))
def enum(*args, **kwargs):
    return enumerate(*args, **kwargs)

def solve(input_fname):
    lines = []
    with open(input_fname) as ifile:
        def ri(): 
            return int(ifile.readline().strip())
        def ris(): 
            return list(map(int, ifile.readline().strip().split()))
        for line in ifile:
            lines.append(line.strip())
    pri = dict(zip(string.ascii_lowercase + string.ascii_uppercase,
    range(1,53)))

    total = 0
    for sack in lines:
        left, right = sack[:len(sack)//2], sack[len(sack)//2:]
        # print(left, right)
        common = set(left).intersection(set(right))
        total += pri[list(common)[0]]
    # return total

    total = 0
    for i in range(0, len(lines), 3):
        s1, s2, s3 = lines[i:i+3]
        badge = list(set(s1).intersection(s2).intersection(s3))[0]
        # print(badge, "".join(lines[i:i+3]).count(badge))
        total += pri[badge]
    return total







if __name__ == "__main__":
    print(solve("../inputs/day3.in"))
