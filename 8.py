import sys
import math
from collections import defaultdict


with open(sys.argv[1],'r') as f:
    lines = [line.strip() for line in f.readlines()]

R = len(lines)
C = len(lines[0])
G = defaultdict(int)
for r in range(R):
    for c in range(C):
        G[(r,c)] = lines[r][c]

def trees(p):
    others = defaultdict(list)
    others['top'].extend([G[(r,p[1])] for r in range(p[0])][::-1])
    others['bottom'].extend(G[(r,p[1])] for r in range(p[0]+1,R))
    others['right'].extend(G[(p[0],c)] for c in range(p[1]+1,C))
    others['left'].extend([G[(p[0],c)] for c in range(p[1])][::-1])
    return others

def spot(v,l):
    cnt = 0
    for i in range(len(l)):
        cnt += 1
        if v <= l[i]:
            return cnt
    return cnt

cnt = 0
score = defaultdict(int)
for r in range(1,R-1):
    for c in range(1,C-1):
        others = trees((r,c))
        score[(r,c)] =  math.prod([spot(G[(r,c)],v) for v in others.values()])
        if any(all(G[(r,c)] > v for v in values) for values in others.values()):
            cnt += 1


arround = (R+C)*2 - 4
part1 = cnt + arround
print(part1)
print(max(score.values()))
