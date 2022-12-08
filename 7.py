import sys
from collections import defaultdict


with open(sys.argv[1],'r') as f:
    lines = [line.strip() for line in f.readlines()]

path = []
storage = defaultdict(int)
for line in lines:
    token = line.split()
    if token[0] == '$' and token[1] == 'cd':
        if token[2] == '..':
            path.pop()
        else:
            path.append(token[2])
    if token[0] == '$' and token[1] == 'ls':
        pass
    else:
        print(path)
        try:
            size = int(token[0])
            for i in range(0,len(path)):
                storage['/'.join(path[:i+1])] += size
        except ValueError:
            pass

part1 = sum([s for s in storage.values() if s < 100000])
print(part1)

TOTAL = 70000000
OUTER = storage['/']
UNUSED = TOTAL - OUTER
REQUIRE = 30000000 - UNUSED
print(min([s for s in storage.values() if s > REQUIRE]))
