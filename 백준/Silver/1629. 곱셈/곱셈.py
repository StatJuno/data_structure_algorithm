import sys
input = sys.stdin.readline

def power(a, b, c):
    if b == 0:
        return 1
    if b % 2 == 0:
        half = power(a, b // 2, c)
        return (half * half) % c 
    else:
        return (power(a, b-1, c) * a) % c
        
A, B, C = map(int, input().split())

print(power(A, B, C))