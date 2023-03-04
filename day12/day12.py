#!/usr/bin/env python3
from collections import deque


def getnei(r, c):
    nei = []
    for dr, dc in ((-1, 0), (1, 0), (0, 1), (0, -1)):
        if 0 <= r+dr < maxr and 0 <= c+dc < maxc:
            if G[(r+dr, c+dc)] <= G[(r, c)] + 1:
                nei.append((r+dr, c+dc))
    return nei


def path(q):
    locked = set()
    while q:
        step, r, c = q.popleft()
        if (r, c) == target:
            return step
        if (r, c) in locked:
            continue
        locked.add((r, c))
        for p in getnei(r, c):
            q.append((step + 1, p[0], p[1]))


with open('input.txt', 'r') as f:
    lines = f.readlines()


maxr = len(lines)
maxc = len(lines[0].strip())
G = {}
queue = deque()
queue2 = deque()
for r, line in enumerate(lines):
    for c, char in enumerate(line.strip()):
        if char == 'S':
            queue.append((0, r, c))
            queue2.append((0, r, c))
            G[(r, c)] = 0
        elif char == 'a':
            queue2.append((0, r, c))
            G[(r, c)] = 0
        elif char == 'E':
            target = (r, c)
            G[(r, c)] = 25
        else:
            G[(r, c)] = ord(char) - ord('a')

print(f'Part1: {path(queue)}')
print(f'Part2: {path(queue2)}')
