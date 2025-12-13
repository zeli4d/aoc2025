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
        last_e = 0
        result = 0
        # last_e = fresh[0][1]
        # result = fresh[0][1] - fresh[0][0] + 1
        for (s, e) in fresh:
            print("last_e = {}, s = {}, e = {}".format(last_e, s, e))

            if s > last_e:
                s_calc = s
                e_calc = e
            else:
                s_calc = last_e + 1
                e_calc = e
            if e > last_e:
                last_e = e

            # print("s_calc = ", s_calc)
            # print("e_calc = ", e_calc)
            if s_calc <= e_calc:
                inter = e_calc - s_calc + 1
                result += inter
            # print(" inter = ", inter)
            print()

    print("\nresult = ", result)


b()
