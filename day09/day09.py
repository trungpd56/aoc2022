#!/usr/bin/env python3
import math

direction = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}


def solve(n):
    knots = [(0, 0)] * n
    visited = {(0, 0)}
    for line in lines:
        line = line.strip()
        cmd, val = line[0], int(line[1:])
        m = direction[cmd]
        for i in range(val):
            # move head
            knots[0] = knots[0][0] + m[0], knots[0][1] + m[1]

            # move tail
            for t in range(1, len(knots)):
                delta = (
                    knots[t - 1][0] - knots[t][0],
                    knots[t - 1][1] - knots[t][1],
                )
                if abs(delta[0]) > 1 or abs(delta[1]) > 1:
                    x, y = knots[t]
                    if delta[0]:
                        x += math.copysign(1, delta[0])
                    if delta[1]:
                        y += math.copysign(1, delta[1])
                    knots[t] = (x, y)
                if t == len(knots) - 1:
                    visited.add(knots[t])
    return len(visited)


with open("input.txt", "r") as f:
    lines = f.readlines()


part1 = solve(2)
print(f"Part1: {part1}")

part2 = solve(10)
print(f"Part2: {part2}")
