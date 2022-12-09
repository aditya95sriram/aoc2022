import numpy as np

def solve(input_fname):
    delta = dict(R=1, L=-1, U=1j, D=-1j)
    h_moves = []
    with open(input_fname) as ifile:
        for line in ifile:
            d, n = line.strip().split()
            h_moves.append((d, int(n)))

    # use complex numbers to represent 2d point
    H = 0+0j
    # t = 0+0j  # [part 1]
    Ts = [0+0j for _ in range(9)]  # [part 2]
    visited = {0+0j}
    for d, n in h_moves:
        for _ in range(n):
            H += delta[d]
            # for [part 1] unfold following loop one time
            follow = H
            for i, Ti in enumerate(Ts):
                diff = follow-Ti
                dx, dy = diff.real, diff.imag
                if abs(dy) > 1 or abs(dx) > 1:
                    dx_sign, dy_sign = np.sign(dx), np.sign(dy)
                    Ti += min(1, abs(dx))*dx_sign +\
                          min(1, abs(dy))*dy_sign*1j
                    Ts[i] = Ti
                follow = Ti  # next knot follows current knot
            visited.add(Ts[-1])

    return len(visited)

if __name__ == "__main__":
    print(solve("../inputs/day9.in"))
