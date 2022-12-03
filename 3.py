import sys
import string


with open(sys.argv[1],'r') as f:
    lines = [line.strip() for line in f.readlines()]

bag = []
for line in lines:
    x = int(len(line) / 2)
    bag1 = set(line[x:])
    bag2 = set(line[:x])
    bag.extend(bag1 & bag2)

def priority(x):
    if x in string.ascii_lowercase:
        return ord(x) - 96
    elif x in string.ascii_uppercase:
        return ord(x) - 38
    else:
        raise Exception("value error")

part1 = sum(priority(x) for x in bag)
print(part1)

bag = []
n  = 3
for n in range(0,len(lines),3):
    l1,l2,l3 = lines[n:n+3]
    bag1 = set(l1)
    bag2 = set(l2)
    bag3 = set(l3)
    bag.extend(bag1 & bag2 & bag3)

part2 = sum(priority(x) for x in bag)
print(part2)
