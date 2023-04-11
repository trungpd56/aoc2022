#!/usr/bin/env python3


def score(c):
    if "a" <= c <= "z":
        return ord(c) - ord("a") + 1
    return ord(c) - ord("A") + 27


with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

priority = 0
for line in lines:
    mid = len(line) // 2
    common = set(line[:mid]) & set(line[mid:])
    priority += sum(score(c) for c in common)

priority2 = 0
for g in zip(*[iter(lines)] * 3):
    common = set(g[0]) & set(g[1]) & set(g[2])
    priority2 += sum(score(c) for c in common)

part1 = priority
print(f"Part1: {part1}")

part2 = priority2
print(f"Part2: {part2}")
