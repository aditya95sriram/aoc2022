#!/usr/bin/python

import numpy as np

def solve(input_fname):
    cmds = []
    with open(input_fname) as ifile:
        for line in ifile:
            if line.startswith("addx"):
                cmd, v = line.split()
                cmds.append((cmd, int(v)))
            else:
                cmds.append((line.strip(), 0))

    # program variables
    cycle = 0
    pc = 0
    regx = 1
    setx = 1
    fin = 0

    # [part 1]
    total = 0
    timestamps = [20, 60, 100, 140, 180, 220]

    # [part 2]
    sprite = 1  # (for readability, even though same as regx)
    crt = -np.ones(240, dtype=int)

    while True:
        cycle += 1
        if cycle == fin + 1:  # update register x
            # end of prev cycle
            regx = setx
            sprite = regx  # [part 2]

            # start of next cycle
            if pc >= len(cmds):
                # end of program
                break
            cmd, v = cmds[pc]
            pc += 1
            if cmd == "noop":
                fin = cycle
                setx = regx
            elif cmd == "addx":
                fin = cycle + 1
                setx = regx + v

        # [part 1] update total at special timestamps
        if cycle in timestamps:
            total += cycle * regx
        
        # [part 2] check and draw crt pixel
        if (cycle-1)%40 in [sprite-1, sprite, sprite+1]:
            crt[cycle-1] = 1
        else:
            crt[cycle-1] = 0

    #return total  # [part 1]
    # render crt    # [part 2]
    return(
        "\n".join(
            "".join([".#?"[b] for b in row])
            for row in crt.reshape(6, 40)
        )
    )

if __name__ == "__main__":
    print(solve("../inputs/day10.in"))