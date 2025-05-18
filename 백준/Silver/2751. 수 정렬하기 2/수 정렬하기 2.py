import sys
N = int(sys.stdin.readline())
a = []

for i in range(N):
    a.append(int(sys.stdin.readline()))
    
a = sorted(a)
for i in range(N):
    print(a[i])