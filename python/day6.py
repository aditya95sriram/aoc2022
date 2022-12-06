#!/usr/bin/python3

def solve(input_fname):
    with open(input_fname) as ifile:
        for line in ifile:
            N = 4  # set N to 14 for part 2
            for i, elems in enumerate(zip(*(line[j:] for j in range(N)))):
                if len(set(elems)) == N:
                    return i + N

if __name__ == "__main__":
    print(solve("../inputs/day6.in"))
