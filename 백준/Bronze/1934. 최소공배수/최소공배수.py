import sys
import math
T = int(sys.stdin.readline())

for i in range(T):
    a, b = map(int, sys.stdin.readline().split())
    print(math.lcm(a,b))
            