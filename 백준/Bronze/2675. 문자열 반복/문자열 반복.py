import sys
T = int(sys.stdin.readline())

for i in range(T):
    S, R = sys.stdin.readline().split()
    for j in list(R):
        print(j * int(S), end = '')
    print()

