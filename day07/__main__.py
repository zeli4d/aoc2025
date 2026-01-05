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
                        new_beams.add(b - 1)
                        new_beams.add(b + 1)
                        new_beams.remove(b)
                        result += 1
                beams = new_beams
            # print(input)
            # print(beams)

    print("\nresult = ", result)


def b():
    result = 1
    beams = list()
    with (open("input07.txt") as f):
        for line in f:
            # input.append(line.strip().split())
            input = list(line.strip())
            if len(beams) == 0:
                beams = [0] * len(input)
                beams[input.index("S")] = 1
            else:
                new_beams = deepcopy(beams)
                for i in range(len(beams)):
                    if beams[i] > 0 and input[i] == "^":
                        new_beams[i - 1] += new_beams[i]
                        new_beams[i + 1] += new_beams[i]
                        new_beams[i] = 0
                        input[i - 1] = "|"
                        input[i + 1] = "|"
                    # else:
                    #     input[i] = "|"
                # print("".join(input), beams)
                beams = new_beams
            # print(input)
            # print(beams)
    result = sum(beams)

    print("\nresult = ", result)


b()
