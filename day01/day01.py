#!/usr/bin/env python3

with open("input.txt", "r") as f:
    data = f.read().strip().split("\n\n")

elves = []
for d in data:
    calo = sum(map(int, d.split("\n")))
    elves.append(calo)

sort_elves = sorted(elves, reverse=True)
part1 = sort_elves[0]
print(f"Part1: {part1}")

part2 = sum(sort_elves[:3])
print(f"Part2: {part2}")
