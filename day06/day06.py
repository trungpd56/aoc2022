#!/usr/bin/env python3


def solve(line, n):
    for i in range(n, len(line)):
        marker = set(line[i - n: i])
        if len(marker) == n:
            return i


with open("input.txt", "r") as f:
    line = f.read().strip()

part1 = solve(line, 4)
print(f"Part1: {part1}")

part2 = solve(line, 14)
print(f"Part2: {part2}")
