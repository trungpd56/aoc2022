#!/usr/bin/env python3
from collections import defaultdict

with open("input.txt", "r") as f:
    lines = f.readlines()

path = []
dirs = defaultdict(int)
for line in lines:
    toks = line.split()
    if toks[1] == "ls":
        continue
    elif toks[1] == "cd":
        if toks[2] == "..":
            path.pop()
        else:
            path.append(toks[2])
    else:
        try:
            for i in range(len(path)):
                dirs["/".join(path[: i + 1])] += int(toks[0])
        except ValueError:
            pass

part1 = sum([d for d in dirs.values() if d < 100000])
print(f"Part1: {part1}")

TOTAL = 70000000
REQUIRE = 30000000
USED = TOTAL - dirs["/"]
NEEDED = REQUIRE - USED

part2 = sorted([d for d in dirs.values() if d > NEEDED])[0]
print(f"Part2: {part2}")
