#!/usr/bin/python3

import numpy as np
import networkx as nx

def solve(input_fname):
    lines = []
    start = end = None
    with open(input_fname) as ifile:
        for line_num, line in enumerate(ifile):
            line = line.strip()
            if 'S' in line:
                start = line.find('S'), line_num
                line = line.replace('S', 'a')
            if 'E' in line:
                end = line.find('E'), line_num
                line = line.replace('E', 'z')
            lines.append(list(map(lambda c: ord(c)-ord('a'), line)))
    
    ar = np.array(lines, dtype=int)
    h, w = ar.shape
    
    # construct directed graph with allowed edges
    g = nx.DiGraph()
    for y in range(h):
        for x in range(w):
            cur = ar[y,x]
            g.add_node((x,y))
            if x > 0 and ar[y,x-1] <= cur + 1:
                g.add_edge((x,y), (x-1,y))
            if x < w-1 and ar[y,x+1] <= cur + 1:
                g.add_edge((x,y), (x+1,y))
            if y > 0 and ar[y-1,x] <= cur + 1:
                g.add_edge((x,y), (x,y-1))
            if y < h-1 and ar[y+1,x] <= cur + 1:
                g.add_edge((x,y), (x,y+1))

    # [part 1]
    # return nx.shortest_path_length(g, start, end)

    # [part 2]
    # cutoff is answer from part 1
    dists = nx.single_target_shortest_path_length(g, end, cutoff=462)
    return min(dist for (x,y), dist in dists if ar[y, x]==0)


if __name__ == "__main__":
    print(solve("../inputs/day12.in"))