import sys
N = int(sys.stdin.readline())

s = []
for i in range(N):
    c = sys.stdin.readline().split()
    
    if c[0] == 'push':
        s.append(c[1])
    elif c[0] == 'pop':
        if len(s) == 0:
            print(-1)
        else:
            print(s.pop())
    elif c[0] == 'size':
        print(len(s))
    elif c[0] == 'empty':
        if len(s) == 0:
            print(1)
        else:
            print(0)
    elif c[0] == 'top':
        if len(s) == 0:
            print(-1)
        else:
            print(s[-1])
        
