def a():
    result = 0
    section = 1

    fresh = list()
    with (open("input05.test.txt") as f):
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
    fresh = list()

    with (open("input05.txt") as f):
        for line in f:
            if line.isspace():
                break

            s, e = line.strip().split("-")
            fresh.append((int(s), int(e)))

        fresh.sort()
        print(fresh)
        last_e = fresh[0][1]
        result = fresh[0][1] - fresh[0][0] + 1
        for (s, e) in fresh[1:]:
            print(last_e, s,e)
            if s < last_e:
                s = last_e
            if e > last_e:
                result += e - s + 1
                last_e = e + 1

    print("\nresult = ", result)


b()
