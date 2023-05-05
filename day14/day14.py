#!/usr/bin/env python3

with open("input.txt", "r") as f:
    lines = f.readlines()


def solve(lines, part2=False):
    grid = set()
    for line in lines:
        toks = line.strip().split(" -> ")
        prev = None
        for tok in toks:
            c, r = map(int, tok.split(","))
            if prev is None:
                prev = (c, r)
                continue
            minc, maxc = min(prev[0], c), max(prev[0], c)
            minr, maxr = min(prev[1], r), max(prev[1], r)
            prev = (c, r)
            for r in range(minr, maxr + 1):
                for c in range(minc, maxc + 1):
                    grid.add((c, r))

    last_row = max(r for c, r in grid)

    num = 0
    while True:
        sand = (500, 0)
        while True:
            c, r = sand
            if (c, r + 1) not in grid:
                sand = (c, r + 1)
            elif (c - 1, r + 1) not in grid:
                sand = (c - 1, r + 1)
            elif (c + 1, r + 1) not in grid:
                sand = (c + 1, r + 1)
            else:
                grid.add(sand)
                break
            if sand[1] == last_row + 1:
                if not part2:
                    return num
                grid.add(sand)
                break
        num += 1
        if sand == (500, 0):
            return num


part1 = solve(lines)
print(f"Part1: {part1}")

part2 = solve(lines, part2=True)
print(f"Part2: {part2}")
