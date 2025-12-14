import math
from copy import deepcopy


def a():
    result = 0
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




def path_rec(pos, map):
    if pos is None:
        # beam start
        return [path_rec(map[0].index("S"), map[1:])]
    else:
        if len(map) == 0:
            return [pos]
        if map[0][pos] == "^":
            #beam split
            return [[pos] + path_rec(pos - 1, map[1:])] + [[pos] + path_rec(pos - 1, map[1:])]
        else:
            #beam pass
            return [pos] + path_rec(pos, map[1:])

#[7,7,6,6,5,5,4,4,3,3,2,2,1,1],[7,7,6,6,5,5,4,4,3,3,2,2,3,3]

def b():
    result = 0
    input = list()
    pathlist = list()
    with (open("input07.test.txt") as f):
        for line in f:
            if line.strip() == "":
                break
            input.append(line.strip())

    pathlist = path_rec(None, input)




    print("-"*100)
    for l in input: print(l)
    for p in pathlist: print(p)

    print("\nresult = ", result)




b()
