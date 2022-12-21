#!/usr/bin/python3

import networkx as nx

def evaluate(d, root="root"):
    subd = d
    if not root == "root":
        subd = d.subgraph(list(nx.ancestors(d, root)) + [root])
    val = dict(subd.nodes(data="const"))

    for node in nx.topological_sort(subd):
        if val[node] is None:
            result = eval(subd.nodes[node]["op"], None, val)
            val[node] = result
            # print(node, "=", result)
        if node == root:
            return val[node]
    # should not reach here
    print("ERROR: no result found for", root, subd.nodes, val)

def solve(input_fname):
    d = nx.DiGraph()
    with open(input_fname) as ifile: 
        for line in ifile:
            name, operation = line.strip().split(": ")
            if operation.isdigit():
                d.add_node(name, const=int(operation))
            else:
                m1, op, m2 = operation.split()
                d.add_node(name, op=operation)
                d.add_edge(m1, name)
                d.add_edge(m2, name)

    # [part 1]
    # return int(evaluate(d))

    # [part 2]
    cur = "root"
    humn = "humn"
    left, _, right = d.nodes[cur]["op"].split()
    if humn in nx.ancestors(d, left):
        cur = left
        target = evaluate(d, right)
    else:
        cur = right
        target = evaluate(d, left)
    while True:
        # print("at node", cur, "target", target)
        left, op, right = d.nodes[cur]["op"].split()
        if humn in nx.ancestors(d, left) or humn == left:
            cur = left
            ready = right
        else:
            cur = right
            ready = left

        if op == "+":
            newtarget = target - evaluate(d, ready)
        elif op == "*":
            newtarget = target / evaluate(d, ready)
        elif op == "-":
            if ready == left:  # target = ready - newtarget
                newtarget = evaluate(d, ready) - target
            else:  # target = newtarget - ready
                newtarget = target + evaluate(d, ready)
        elif op == "/":
            if ready == left:  # target = ready / newtarget
                newtarget = evaluate(d, ready) / target
            else:  # target = newtarget / ready
                newtarget = target * evaluate(d, ready)
        
        target = newtarget
        if cur == humn:
            return int(target)


if __name__ == "__main__":
    print(solve("../inputs/day21.in"))