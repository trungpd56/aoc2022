#!/usr/bin/env python3
from functools import cmp_to_key


def solve(p1, p2):
    if isinstance(p1, int) and isinstance(p2, int):
        if p1 > p2:
            return -1
        elif p1 < p2:
            return 1
        else:
            return 0

    if isinstance(p1, int):
        p1 = [p1]

    if isinstance(p2, int):
        p2 = [p2]

    for p in zip(p1, p2):
        if solve(*p) == 0:
            continue
        return solve(*p)

    if len(p1) > len(p2):
        return -1
    elif len(p1) < len(p2):
        return 1
    else:
        return 0


with open("input.txt", "r") as f:
    pairs = f.read().strip().split("\n\n")

cnt = 0
for i, pair in enumerate(pairs, 1):
    pair = pair.split("\n")
    p1, p2 = map(eval, pair)
    if solve(p1, p2) == 1:
        cnt += i

part1 = cnt
print(f"Part1: {part1}")

packets = [eval(p) for pair in pairs for p in pair.split("\n")]
packets.extend(([[2]], [[6]]))
sorted_packets = sorted(packets, key=cmp_to_key(solve), reverse=True)
divider1 = sorted_packets.index([[2]]) + 1
divider2 = sorted_packets.index([[6]]) + 1
part2 = divider1 * divider2
print(f"Part2: {part2}")
