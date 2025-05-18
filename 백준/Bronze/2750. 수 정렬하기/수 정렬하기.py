N = int(input())
a= []

for i in range(N):
    a.append(int(input()))

a = sorted(a)
print("\n".join(map(str,a)))