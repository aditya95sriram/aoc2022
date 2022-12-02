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
            lines.append(line.strip())
    
    win = {"A": "Y", "B": "Z", "C": "X"}
    draw = dict(zip("ABC", "XYZ"))
    scores = dict(zip("XYZ", (1,2,3)))
    total = 0
    for round in lines:
        op, me = round.split()
        score = 0
        if me == draw[op]:
            score = scores[me] + 3
        elif me == win[op]:
            score = scores[me] + 6
        else:
            score = scores[me]
        total += score
    
    total = 0
    loss = dict(zip("ABC", "ZXY"))
    for round in lines:
        op, me = round.split()
        if me == "X":
            score = scores[loss[op]]
        elif me == "Y":
            score = scores[draw[op]] + 3
        else:
            score = scores[win[op]] + 6
        total += score
    return total







if __name__ == "__main__":
    print(solve("../inputs/day2.in"))
