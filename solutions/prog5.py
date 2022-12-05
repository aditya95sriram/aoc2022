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
    rows = []
    recon = False
    cols = []
    with open(input_fname) as ifile:
        def ri(): 
            return int(ifile.readline().strip())
        def ris(): 
            return list(map(int, ifile.readline().strip().split()))
        for line in ifile:
            if not line.strip("\n"):
                numcrates = len(rows.pop().split())
                cols = [[] for _ in range(numcrates)]
                print(f"{numcrates} crates")
                for row in rows:
                    for i in range(numcrates):
                        coli = 1 + 4*i
                        if row[coli] != " ":
                            cols[i] = [row[coli]] + cols[i]
                pprint(cols)
                recon = True
                continue
            if not recon:
                rows.append(line.strip("\n"))
            else:
                _, count, _, src, _, dest = line.strip().split()
                count, src, dest = lmapi([count, src, dest])
                # for _ in range(count):
                #    cols[dest-1].append(cols[src-1].pop())
                moving = cols[src-1][-count:]
                del cols[src-1][-count:]
                cols[dest-1].extend(moving)
        return ("".join([col[-1] for col in cols]))








if __name__ == "__main__":
    print(solve("../inputs/day5.in"))
