import re, os, sys
from functools import reduce
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
            lines.append(int(line.strip()))
            # lines.append(line.strip())
    return sum(i for i in lines)








if __name__ == "__main__":
    print(solve("../inputs/day1.in"))
