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
    dirs = nx.DiGraph()
    dirs.add_node("/", size=-1)
    cwd = "/"
    with open(input_fname) as ifile:
        def ri(): 
            return int(ifile.readline().strip())
        def ris(): 
            return list(map(int, ifile.readline().strip().split()))
        output = ifile.read()
        lines = [e for e in output.split("$ ") if e]
        print(lines)
    ctr = 0
    for line in lines:
        cmd, output = line.split("\n", 1)
        print("cmd", repr(cmd))
        if cmd.startswith("cd"):
            _, arg = cmd.split(" ")
            if arg == "..":
                pdir = list(dirs.predecessors(cwd)).pop()
                # print("parent of", cwd, pdir)
                cwd = pdir
            else:
                for succ in dirs.successors(cwd):
                    if succ.split("_")[0] == arg:
                        cwd = succ
                # cwd = dirs.predecessor(cwd)

        else:
            for item in output.split("\n"):
                if not item: continue
                size, name = item.split(" ")
                ctr += 1
                uname = name + "_" + str(ctr)
                if size == "dir":
                    dirs.add_node(uname, size=-1)
                else:
                    dirs.add_node(uname, size=int(size))
                dirs.add_edge(cwd, uname)
                # print(repr(size), repr(name))
    
    print(dirs.edges)
    total = 0
    files = set()
    for node in nx.dfs_postorder_nodes(dirs):
        if dirs.nodes[node]["size"] != -1:
            files.add(node)
            # print("continuing", node)
            continue
        ssizes = [dirs.nodes[succ]["size"] for succ in dirs.successors(node)]
        if not all(e >= 0 for e in ssizes):
            print("ERROR for dir", node)
            print([succ for succ in dirs.successors(node) if dirs.nodes[succ]["size"] < 0])
        total_size = sum(ssizes)
        # print("setting size of", node, "to", total_size)
        # print("succ of", node, list(dirs.successors(node)))
        dirs.nodes[node]["size"] = total_size
        if total_size <= 100000:
            # selected.append(node)
            total += total_size
    print(dirs.nodes(data="size"))
    # print(selected)
    # return sum(dirs.nodes[s]["size"] for s in selected)
    # from networkx.drawing.nx_agraph import write_dot
    # write_dot(dirs, "test.dot")

    # [part 1]
    # return total

    total_space = 70000000
    need_free = 30000000
    occupied = dirs.nodes["/"]["size"]
    unused = total_space - occupied
    to_delete = need_free - unused

    bestsize = 1e10
    bestdir = ""
    for onlydir in set(dirs.nodes) - files:
        sz = dirs.nodes[onlydir]["size"]
        if sz >= to_delete:
            if sz < bestsize:
                bestsize = sz
                bestdir = onlydir
    print("delete", bestdir)
    return bestsize











if __name__ == "__main__":
    print(solve("../inputs/day7.in"))
