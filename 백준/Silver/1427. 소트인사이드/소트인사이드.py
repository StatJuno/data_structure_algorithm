N = int(input())
a= []

for i in str(N):
    a.append(int(i))
    
a = sorted(a, reverse = True)
for i in a:
    print(i, end = '')