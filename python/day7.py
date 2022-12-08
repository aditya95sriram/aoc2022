import networkx as nx

def solve(input_fname):
    lines = []
    dirs = nx.DiGraph()
    dirs.add_node("/", size=-1)
    cwd = "/"

    def getsize(name): return dirs.nodes[name]["size"]

    with open(input_fname) as ifile:
        output = ifile.read()
        lines = [e for e in output.split("$ ") if e]
    
    # reproduce dir structure as digraph
    ctr = 1  # counter for unique file/dir name ids
    for line in lines:
        cmd, output = line.split("\n", 1)
        if cmd.startswith("cd"):
            _, arg = cmd.split(" ")
            if arg == "..":
                pdir = list(dirs.predecessors(cwd)).pop()
                cwd = pdir
            else:
                # find child name (ignoring unique id suffix)
                for succ in dirs.successors(cwd):
                    if succ.split("_")[0] == arg:
                        cwd = succ
        else:
            for item in output.split("\n"):
                if not item: continue
                size, name = item.split(" ")
                uname = name + "_" + str(ctr)
                ctr += 1
                if size == "dir":
                    dirs.add_node(uname, size=-1)
                else:
                    dirs.add_node(uname, size=int(size))
                dirs.add_edge(cwd, uname)
    
    # traverse and compute sizes of directories
    total = 0  # [part 1]
    files = set()
    for node in nx.dfs_postorder_nodes(dirs):
        if getsize(node) != -1:
            files.add(node)
            continue
        children = list(dirs.successors(node))
        total_size = sum(getsize(child) for child in children)
        dirs.nodes[node]["size"] = total_size
        if total_size <= 100000:
            total += total_size
    # print(dirs.nodes(data="size"))
    # return total  # [part 1]

    # [part 2]
    total_space = 70000000
    need_free = 30000000
    occupied = getsize("/")
    unused = total_space - occupied
    to_delete = need_free - unused

    bestsize = 1e10
    bestdir = ""
    for onlydir in set(dirs.nodes) - files:
        sz = getsize(onlydir)
        if sz >= to_delete:
            if sz < bestsize:
                bestsize = sz
                bestdir = onlydir
    return bestsize  # [part 2]

if __name__ == "__main__":
    print(solve("../inputs/day7.in"))
