import sys
A, B, V = map(int, sys.stdin.readline().split())

t = (V-B) / (A-B)
print(int(t) if t == int(t) else int(t)+1)
    