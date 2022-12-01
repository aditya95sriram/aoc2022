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
        for line in ifile:
            lines.append(line.strip())








if __name__ == "__main__":
    print(solve("../inputs/day<DAY>.in"))
