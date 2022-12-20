#!/usr/bin/python3

def mix(lines, repeat=1, mult=1):
    orig = list(enumerate(lines))
    mixed = orig[:]
    n = len(orig)
    for _ in range(repeat):
        # mix
        for i, e in orig:
            cur = mixed.index((i, e))
            assert cur != -1, "index returned -1"
            mixed.remove((i,e))
            if e == 0:
                mixed.insert(cur, (i,e))
            else:
                mixed.insert((cur + e*mult)%(n-1), (i,e))
    
    # collect and sum up coordinates
    final = [e for _, e in mixed]
    start = final.index(0)
    return sum(final[(start + i*1000)%n]*mult for i in (1,2,3))


def solve(input_fname):
    with open(input_fname) as ifile:
        lines = list(map(int,(ifile.readlines())))

    # [part 1]
    # return mix(lines)  # repeat=1, mult=1

    # [part 2]
    return mix(lines, repeat=10, mult=811589153)


if __name__ == "__main__":
    print(solve("../inputs/day20.in"))
