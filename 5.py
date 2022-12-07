import sys
from collections import defaultdict
import string
import re


with open(sys.argv[1],'r') as f:
    data = f.read().rstrip()

crates, insts = data.split('\n\n')
stacks = defaultdict(list)
stacks2 = defaultdict(list)
for line in crates.split('\n')[:-1][::-1]:
    i = 0
    print(line)
    while i < len(line):
        if line[i] in string.ascii_uppercase:
            stacks[(i + 3)//4].append(line[i])
            stacks2[(i + 3)//4].append(line[i])
        i += 1


for line in insts.split('\n'):
    n,src,dst = map(int,re.findall(r'\d+',line))
    for i in range(n):
        stacks[dst].append(stacks[src].pop())
    stacks2[dst].extend(stacks2[src][-n:])
    stacks2[src] = stacks2[src][:-n]

part1 = ''.join([s[-1] for s in stacks.values()])
print(part1)

part2 = ''.join([s[-1] for s in stacks2.values()])
print(part2)
