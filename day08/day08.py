#!/usr/bin/env python3


def sides(r, c):
    top = [trees[i][c] for i in range(r - 1, -1, -1)]
    bottom = [trees[i][c] for i in range(r + 1, len(trees))]
    left = [trees[r][i] for i in range(c - 1, -1, -1)]
    right = [trees[r][i] for i in range(c + 1, len(trees[c]))]
    return top, bottom, left, right


def visible(r, c):
    all_sides = sides(r, c)
    if any(all(trees[r][c] > t for t in s) for s in all_sides):
        return True
    return False


def score(r, c):
    all_sides = sides(r, c)
    score = 1
    for s in all_sides:
        cnt = 0
        for t in s:
            cnt += 1
            if t >= trees[r][c]:
                break
        score *= cnt
    return score


with open("input.txt", "r") as f:
    trees = [list(map(int, list(line.strip()))) for line in f.readlines()]

maxr = len(trees)
maxc = len(trees[0])
cnt = 0
for r in range(1, maxr - 1):
    for c in range(1, maxc - 1):
        if visible(r, c):
            cnt += 1

part1 = cnt + 2 * (maxr + maxc) - 4
print(f"Part1: {part1}")

maxs = 0
for r in range(maxr):
    for c in range(maxc):
        maxs = max(maxs, score(r, c))

part2 = maxs
print(f"Part2: {part2}")
