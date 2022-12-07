import sys


with open(sys.argv[1],'r') as f:
    line = f.read().rstrip()

def mline(line,n):
    for i in range(len(line)-n):
        marker = set(line[i:i+n])
        if len(marker) == n:
            print(i+n)
            return i+n

print(mline(line,4))
print(mline(line,14))
