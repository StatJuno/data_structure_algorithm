N = int(input())
size = list(map(int, input().split()))
T, P = map(int, input().split())
bundle = 0
bundle_sum = 0

for i in range(len(size)):
    if size[i] % T == 0:
        bundle = size[i] // T
    else:
        bundle = size[i] // T + 1
    bundle_sum += bundle
    
print(bundle_sum)
print(N // P, N % P)