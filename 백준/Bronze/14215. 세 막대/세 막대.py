a, b, c = map(int, input().split())

print(a+b+c) if max(a,b,c) < sum([a,b,c])-max(a,b,c) else print(2*(sum([a,b,c])-max(a,b,c))-1)