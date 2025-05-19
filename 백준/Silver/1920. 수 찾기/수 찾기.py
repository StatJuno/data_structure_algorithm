import sys
input = sys.stdin.readline

N = int(input())
A = set(map(int, input().split()))
M = int(input())
l = list(map(int, input().split()))

for _ in l:
    print(1 if _ in A else 0)