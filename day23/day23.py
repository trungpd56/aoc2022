#!/usr/bin/env python3
from collections import defaultdict

move = [
    ((-1, -1), (-1, 0), (-1, 1)),  # north
    ((1, -1), (1, 0), (1, 1)),  # south
    ((-1, -1), (0, -1), (1, -1)),  # west
    ((-1,  1), (0, 1), (1, 1)),  # east
]


def getnei(r, c):
    cnt = 0
    for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):
            if (r+dr, c+dc) in grid:
                cnt += 1
    return cnt


def score(grid):
    maxr = max(r for r, c in grid)
    minr = min(r for r, c in grid)
    maxc = max(c for r, c in grid)
    minc = min(c for r, c in grid)
    return (maxr - minr + 1) * (maxc - minc + 1) - num_elves


with open('input.txt', 'r') as f:
    lines = f.readlines()

grid = set()
num_elves = 0
for r, line in enumerate(lines):
    for c, char in enumerate(line.strip()):
        if char == '#':
            grid.add((r, c))
            num_elves += 1

round = 0
while True:
    next_moves = defaultdict(list)
    for r, c in grid:
        if getnei(r, c) == 1:
            continue
        for m in range(4):
            movable = move[(m + round) % 4]
            if sum(1 for dr, dc in movable if (r+dr, c+dc) in grid) == 0:
                next_moves[(r + movable[1][0], c + movable[1][1])].append((r, c))
                break

    for m in next_moves:
        if len(next_moves[m]) == 1:
            grid.add(m)
            grid.remove(next_moves[m][0])

    round += 1
    if round == 10:
        part1 = score(grid)

    if len(next_moves) == 0:
        break

print(f'Part1: {part1}')

part2 = round
print(f'Part2: {part2}')
