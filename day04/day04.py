#!/usr/bin/env python3


def gen_set(s):
    x1, x2 = map(int, s.split("-"))
    return set(range(x1, x2 + 1))


with open("input.txt", "r") as f:
    lines = f.readlines()

cnt = 0
cnt2 = 0
for line in lines:
    g1, g2 = map(gen_set, line.strip().split(","))
    if g1.issuperset(g2) or g2.issuperset(g1):
        cnt += 1
    if len(g1 & g2) > 0:
        cnt2 += 1

part1 = cnt
print(f"Part1: {part1}")

part2 = cnt2
print(f"Part2: {part2}")
