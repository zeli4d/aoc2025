import math


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
    data_in = list()
    linelen = list()

    with (open("input06.txt") as f):
        for line in f:
            data_in.append(list(line))

        for l in data_in:
            linelen.append(len(l))
        maxlen = max(linelen)
        row_len = len(data_in)
        # cycle all columns
        prob_numbers = list()

        oper = ''
        # loop columns left to tight
        for col_ix in range(maxlen):
            num = ''
            # loop each row in column
            for row_ix in range(row_len):
                # avoid short end
                if col_ix < linelen[row_ix]:
                    # skip emptu fields
                    if data_in[row_ix][col_ix].strip() != '':
                        # decide number/operator
                        if row_ix == row_len - 1:
                            oper = data_in[row_ix][col_ix]
                        else:
                            num += data_in[row_ix][col_ix]
                    # print(data_in[row_ix][col_ix])
            if num != '':
                prob_numbers.append(int(num))
            else:
                print(prob_numbers)
                print(oper)
                print("----------")
                if oper == '+':
                    prob_res = sum(prob_numbers)
                    print(prob_res)
                elif oper == '*':
                    prob_res = math.prod(prob_numbers)
                    print(prob_res)

                result += prob_res
                prob_numbers.clear()
#7858808482092

    print(data_in)
    print()




    print("\nresult = ", result)


b()
