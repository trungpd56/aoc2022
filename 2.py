import sys


with open(sys.argv[1],'r') as f:
    lines = [line.strip().split() for line in f.readlines()]

score = {
    'X': {'A':3, 'B': 0 , 'C': 6, 's': 1},
    'Y': {'A':6, 'B': 3 , 'C': 0, 's': 2},
    'Z': {'A':0, 'B': 6 , 'C': 3, 's': 3}
    }

part1 = sum([score[w2]['s'] + score[w2][w1] for w1,w2 in lines])
print(part1)

stra = {
    'A': {'X':'Z', 'Y':'X', 'Z':'Y'},
    'B': {'X':'X', 'Y':'Y', 'Z':'Z'},
    'C': {'X':'Y', 'Y':'Z', 'Z':'X'}
}

fround = [(w1,stra[w1][w2]) for w1,w2 in lines]
part2 = sum([score[w2]['s'] + score[w2][w1] for w1,w2 in fround])
print(part2)
