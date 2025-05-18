N, k = map(int, input().split())
s = list(map(int, input().split()))
s = sorted(s, reverse = True)

print(s[k-1])