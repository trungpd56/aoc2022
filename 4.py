import sys
import re


with open(sys.argv[1],'r') as f:
    lines = [line.strip() for line in f.readlines()]

cnt = 0
cnt2 = 0
for line in lines:
    x1,x2,y1,y2 = map(int,re.findall(r'\d+',line))
    el1 = set(range(x1,x2+1))
    el2 = set(range(y1,y2+1))
    if el1.issubset(el2) or el2.issubset(el1):
        cnt += 1
    if any(e in el2 for e in el1):
        cnt2 += 1

print(cnt)
print(cnt2)
