import sys
input = sys.stdin.readline
M = int(input())
s = set()
for i in range(M):
    line = list(input().split())
    if len(line) == 1:
        if line[0] == "all":
            s = set({j for j in range(1,21)})
        else:
            s = set()
    else:
        f, x = line[0], line[1]
        x = int(x)
        if f == "add":
            s.add(x)
        elif f == "remove":
            s.discard(x)
        elif f == "check":
            print(1 if x in s else 0)
        elif f == "toggle":
            if x in s:
                s.discard(x)
            else:
                s.add(x)
    