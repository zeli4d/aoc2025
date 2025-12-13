def a():
    result = 0

    input = list()
    with (open("input06.txt") as f):
        for line in f:
            input.append(line.strip().split())

        rows = len(input)-1
        for c in range(len(input[rows])):
            if input[rows][c] == '+':
                inter = 0
                for r in range(rows):
                    inter += int(input[r][c])
            else:
                inter = 1
                for r in range(rows):
                    inter *= int(input[r][c])
            result += inter
    print(input)

    print("\nresult = ", result)


def b():
    result = 0

    print("\nresult = ", result)


a()
