import sys
a = []

for i in range(9):
    A = int(sys.stdin.readline())
    a.append(A)

print(max(a))
print(a.index(max(a))+1)