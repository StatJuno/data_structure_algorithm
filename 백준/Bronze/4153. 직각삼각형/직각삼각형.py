while 1:
    a, b, c = map(int, input().split())
    if a + b + c == 0:
        break
    l = [a,b,c]
    m = max(l)
    l.remove(m)
    if l[0]**2 + l[1]**2 == m**2:
        print('right')
    else:
        print('wrong')