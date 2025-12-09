def a():
    result = 0

    with open("input02.txt") as f:
        line = f.readline()

        for itm_range in line.split(","):
            print(itm_range)
            # skip invalids starting with 0
            if itm_range[0] == "0":
                continue
            boundaries = itm_range.split("-")
            for item in range(int(boundaries[0]), int(boundaries[1])+1):
                l = len(str(item))
                if str(item)[0:l//2] == str(item)[l//2:]:
                    result += item

    print("result(a) = ", result)


def b():
    result = 0

    with open("input02.txt") as f:
        line = f.readline()
        # split to ranges
        for itm_range in line.split(","):
            # print(itm_range)
            # skip invalids starting with 0
            if itm_range[0] == "0":
                continue
            boundaries = itm_range.split("-")
            # iterate in ranges
            for item in range(int(boundaries[0]), int(boundaries[1])+1):

                itemt = str(item)

                invalid = False
                totallen = len(itemt)

                # iterate all block sizes upt to len/2 (at least 2 identical blocks)
                for blklen in range(1, totallen // 2 + 1):
                    # print("blklen = {}, invalid = {}", blklen, invalid)
                    # define 1st block
                    pat = itemt[0:blklen]
                    for e in range(blklen, totallen, blklen):
                        # print("pat = {} item =  {}", pat, itemt[e:e + blklen])
                        # if block is same as previous, mark as invalid
                        if pat == itemt[e:e + blklen]:
                            invalid = True
                        else:
                            # or not (this is necessary, because 1st and second can match but 3rd not)
                            invalid = False
                        if not invalid:
                            # exit block size if not invalid
                            break
                    if invalid:
                        # do not teas another block size if the last one is prooves invalid
                        break
                if invalid:
                    # print("invalid id = ", item)
                    result += item

    print("result(a) = ", result)

# a()
b()

