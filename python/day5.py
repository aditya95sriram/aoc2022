#!/usr/bin/python3

def lmapi(*args, **kwargs):
    return list(map(int, *args, **kwargs))

def solve(input_fname):
    rows = []
    stacks = []
    recon = False
    with open(input_fname) as ifile:
        for line in ifile:
            if not line.strip("\n"):  # blank line
                numcrates = len(rows.pop().split())
                stacks = [[] for _ in range(numcrates)]
                print(f"{numcrates} crates")
                for row in rows:
                    for stackidx in range(numcrates):
                        textcol = 1 + 4*stackidx
                        if row[textcol] != " ":
                            stacks[stackidx] = [row[textcol]] + stacks[stackidx]
                recon = True
                continue

            if not recon:
                rows.append(line.strip("\n"))
            else:
                _, count, _, src, _, dest = line.strip().split()
                count, src, dest = lmapi([count, src, dest])
                # [part 1] transfer in reverse order
                # for _ in range(count):
                #    stacks[dest-1].append(stacks[src-1].pop())

                # [part 2] transfer in same order
                moving = stacks[src-1][-count:]
                del stacks[src-1][-count:]
                stacks[dest-1].extend(moving)
    
        return "".join([stack[-1] for stack in stacks])

if __name__ == "__main__":
    print(solve("../inputs/day5.in"))
