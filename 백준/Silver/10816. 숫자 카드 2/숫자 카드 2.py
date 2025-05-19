import sys
input = sys.stdin.readline

N = int(input())
M = list(map(int, input().split()))
A = int(input())
l = list(map(int, input().split())) 

dic = {}
for i in M:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
    
for j in l:
    if j in dic:
        print(dic[j], end = ' ')
    else:
        print(0, end = ' ')