import math
from copy import deepcopy


def a():
    result = 0

    # input = list()
    beams = set()
    with (open("input07.txt") as f):
        for line in f:
            # input.append(line.strip().split())
            input = list(line.strip())
            if len(beams) == 0:
                 beams.add(input.index("S"))
            else:
                new_beams = deepcopy(beams)
                for b in beams:
                    if input[b] == "^":
                        new_beams.add(b-1)
                        new_beams.add(b+1)
                        new_beams.remove(b)
                        result += 1
                beams = new_beams
            # print(input)
            # print(beams)

    print("\nresult = ", result)


def b():
    result = 0
    with (open("input07.txt") as f):
        for line in f:
            input.append(line.strip().split())

    # for l in input: print(l)

    print("\nresult = ", result)


b()
