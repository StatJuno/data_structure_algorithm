import sys
N = int(sys.stdin.readline())

s = []
for i in range(N):
    c = sys.stdin.readline().split()
    
    if c[0] == '1':
        s.append(c[1])
    elif c[0] == '2':
        if len(s) == 0:
            print(-1)
        else:
            print(s.pop())
    elif c[0] == '3':
        print(len(s))
    elif c[0] == '4':
        if len(s) == 0:
            print(1)
        else:
            print(0)
    elif c[0] == '5':
        if len(s) == 0:
            print(-1)
        else:
            print(s[-1])
        
