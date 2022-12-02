import sys


with open(sys.argv[1],'r') as f:
    elf = f.read().strip().split('\n\n')

elf = [list(map(int,e.split())) for e in elf]
calo = sorted([sum(e) for e in elf],reverse=True)
print(calo[0])
print(sum(calo[:3]))
