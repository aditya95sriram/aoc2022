import re, os, sys
from functools import reduce
from itertools import combinations as comb, permutations as perm, combinations_with_replacement as combr
from operator import itemgetter
from pprint import pprint
from math import *
from collections import defaultdict
import networkx as nx
import numpy as np

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
            lines.append(line.strip().split(","))

    count = 0
    for line in lines:
        s1, s2 = line
        a,b = lmapi(s1.split("-"))
        a1 = set(range(a,b+1))
        x,y = lmapi(s2.split("-"))
        a2 = set(range(x,y+1))
        # if a1 | a2 == a1 or a1 | a2 == a2:
            # count += 1
        if a1.intersection(a2):
            count += 1
    return count





if __name__ == "__main__":
    print(solve("../inputs/day4.in"))
