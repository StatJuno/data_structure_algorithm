T = int(input())

for i in range(T):
    a = str(input())
    s = []
    for j in a:
        if j == '(':
            s.append(j)
        elif j == ')':
            if len(s) != 0:
                s.pop()
            else:
                s.append(j)
                break
    if len(s) != 0: 
        print("NO")
    else:
        print("YES")
            