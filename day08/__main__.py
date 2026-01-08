import math
import sys
from copy import deepcopy

boxlist = list()


def a():
    result = 0
    with (open("input08.txt") as f):
        for line in f:
            # boxlist.append(list(map(int, line.split(','))))
            boxlist.append(tuple(map(int, line.strip().split(','))))

    connections = 1000
    conn_list = set()
    networks = list()
    while connections > 0:
        min_dist = float(sys.maxsize)
        conn = tuple()
        for node_a in boxlist:
            for node_b in boxlist[boxlist.index(node_a) + 1:]:
                dist = math.dist(node_a, node_b)
                if dist <= min_dist and not conn_list.__contains__((node_a, node_b)):
                    min_dist = dist
                    conn = (node_a, node_b)

                # print(node_a, node_b, dist, min_dist)
        conn_list.add(conn)

        matched = False
        for n in networks:
            if set(n) >= set(conn):
                matched = True
                connections -= 1
                break
            if set(n) & set(conn) != set():
                networks.remove(n)
                # networks.append(set(n)|set(conn))
                conn = tuple(set(n) | set(conn))
                # matched = True
                # connections -= 1
        if not matched:
            networks.append(set(conn))
            connections -= 1

    # print(boxlist)
    for c in conn_list: print(c, math.dist(c[0], c[1]))

    networks.sort(key=lambda x: len(x), reverse=True)

    print("_" * 50)
    result = math.prod(len(i) for i in (networks[:3]))
    for net in networks: print(net)

    print("\nresult = ", result)


def b():
    result = 0
    with (open("input08.txt") as f):
        for line in f:
            # boxlist.append(list(map(int, line.split(','))))
            boxlist.append(tuple(map(int, line.strip().split(','))))

    conn_list = list()
    networks = list()
    last_conn = tuple()

    for node_a in boxlist:
        # create default list of single node networks
        networks.append({node_a})
        # calculate all 2 node distances
        for node_b in boxlist[boxlist.index(node_a) + 1:]:
            conn_list.append((node_a, node_b, math.dist(node_a, node_b)))
    # sort connection distances
    conn_list.sort(key=lambda x: x[2])

    for conn in conn_list:
        print(conn)
        last_conn = conn
        to_add = set()
        to_remove = list()
        for a in networks:
            if a.isdisjoint({conn[0], conn[1]}): continue
            if to_add == set():
                to_add = a | {conn[0], conn[1]}
            else:
                to_add |= a
            to_remove.append(a)
        networks = [item for item in networks if item not in to_remove]
        networks.append(to_add)

        if len(networks) == 1: break

    print("last_conn =", last_conn)
    result = last_conn[0][0] * last_conn[1][0]
    print("\nresult = ", result)


b()
