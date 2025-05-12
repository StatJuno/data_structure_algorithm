import sys
number = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
N, B = sys.stdin.readline().split()
    
answer = 0
for i, val in enumerate(N[::-1]):
    answer += int(B)**i * number.index(val)
print(answer)