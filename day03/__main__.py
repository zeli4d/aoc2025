def a():
    result = 0
    with (open("input03.txt") as f):
        for line in f:
            l1 = 0
            n1 = "0"
            n2 = "0"
            for pos in range(0, len(line.strip()) - 1):
                # print("N1", pos, line[pos], n1)
                if line[pos] > n1:
                    n1 = line[pos]
                    l1 = pos
            for pos in range(l1 + 1, len(line.strip())):
                # print("N2", pos, line[pos], n2)
                if line[pos] > n2:
                    n2 = line[pos]

            # print(line.strip(), n1+n2)

            result += int(n1 + n2)

    print("\nresult = ", result)


a()
