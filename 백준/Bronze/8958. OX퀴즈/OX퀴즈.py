N = int(input())

for i in range(N):
    t = input()
    s,ss = 0, 0
    for j in t:
        if j =='O':
            s += 1 
        else:
            s= 0
        ss += s
    print(ss)
    