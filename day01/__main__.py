class Dial:
    position = 50
    first_pos = 0
    last_pos = 99

    def rotate(self, ticks):
        self.position = (self.position + ticks) % 100


def a():
    d = Dial()

    zero_cnt = 0

    with open("input01.txt") as f:
        for line in f:
            if line.strip()[0] == "L":
                d.rotate(-1 * int(line.strip()[1::]))
            elif line.strip()[0] == "R":
                d.rotate(int(line.strip()[1::]))
            else:
                print("Wrong direction {line.strip()[0]}")
            if d.position == 0:
                zero_cnt += 1

    print(zero_cnt)


def b():
    dial = 50
    zero_total = 0
    direction = 0
    # with open("input_test.txt") as f:
    with open("input01.txt") as f:
        for line in f:
            ticks = int(line.strip()[1::])
            if line.strip()[0] == 'L':
                direction = -1
            elif line.strip()[0] == 'R':
                direction = 1
            else:
                print("Wrong direction {line.strip()[0]}")

            print("dial = {}, line = {}, zero_total = {}".format(dial, line.strip(), zero_total))
            print("ticks = {}, direction = {}".format(ticks, direction))
            for t in range(direction, direction * ticks + direction, direction):
                dial += direction
                # print("dial = {}".format(dial))
                if dial == 100:
                    dial = 0
                if dial == -1:
                    dial = 99
                if dial == 0:
                    zero_total += 1

            print("dial = {}, line = {}, zero_total = {}".format(dial, line.strip(), zero_total))


b()
