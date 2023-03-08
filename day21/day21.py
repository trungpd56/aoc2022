#!/usr/bin/env python3

def solve(m):
    try:
        return int(info[m][0])
    except ValueError:
        pass

    if info[m][1] == '+':
        return solve(info[m][0]) + solve(info[m][2])
    if info[m][1] == '-':
        return solve(info[m][0]) - solve(info[m][2])
    if info[m][1] == '/':
        return solve(info[m][0]) / solve(info[m][2])
    if info[m][1] == '*':
        return solve(info[m][0]) * solve(info[m][2])


def solve2(m, humn):
    if m == 'humn':
        return humn
    try:
        return int(info[m][0])
    except ValueError:
        pass

    if m == 'root':
        v1 = solve2(info[m][0], humn)
        v2 = solve2(info[m][2], humn)
        return (v1 == v2, v1, v2)

    if info[m][1] == '+':
        return solve2(info[m][0], humn) + solve2(info[m][2], humn)
    if info[m][1] == '-':
        return solve2(info[m][0], humn) - solve2(info[m][2], humn)
    if info[m][1] == '/':
        return solve2(info[m][0], humn) / solve2(info[m][2], humn)
    if info[m][1] == '*':
        return solve2(info[m][0], humn) * solve2(info[m][2], humn)


with open('input.txt', 'r') as f:
    lines = f.readlines()

info = {}
for line in lines:
    toks = line.strip().split(': ')
    info[toks[0]] = toks[1].split()

part1 = solve('root')
print(f'Part1: {part1}')


lo = -1e20
hi = 1e20
while lo <= hi:
    mid = (hi + lo) // 2
    eq, v1, v2 = solve2('root', mid)
    if eq:
        part2 = mid
        break
    elif v1 - v2 > 0:
        lo = mid + 1
    else:
        hi = mid - 1

print(f'Part2: {part2}')
