#!/usr/bin/env python3
from collections import defaultdict
import re

with open("input.txt", "r") as f:
    raws, steps = f.read().split("\n\n")

crates = defaultdict(list)
crates2 = defaultdict(list)

for r in raws.split("\n")[:-1][::-1]:
    for i, c in enumerate(r):
        if c not in "[] ":
            crates[i // 4 + 1].append(c)
            crates2[i // 4 + 1].append(c)

for step in steps.strip().split("\n"):
    n, src, dst = map(int, re.findall(r"\d+", step))
    for i in range(n):
        crates[dst].append(crates[src].pop())
    crates2[dst].extend(crates2[src][-n:])
    crates2[src] = crates2[src][:-n]


part1 = "".join(v[-1] for v in crates.values())
print(f"Part1: {part1}")

part2 = "".join(v[-1] for v in crates2.values())
print(f"Part2: {part2}")
