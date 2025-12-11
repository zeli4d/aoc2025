def a():
    result = 0
    section = 1

    fresh = list()
    with (open("input05.txt") as f):
        for line in f:
            if line.isspace():
                break
            s, e = line.strip().split("-")
            fresh.append((int(s), int(e)))

        fresh.sort()

        for line in f:
            for (s, e) in fresh:
                if int(line.strip()) > s and int(line.strip()) <= e:
                    result += 1
                    break

    print("\nresult = ", result)


def b():
    result = 0

    print("\nresult = ", result)


a()
