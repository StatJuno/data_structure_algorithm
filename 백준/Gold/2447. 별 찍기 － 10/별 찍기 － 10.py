import sys

def starpoint(n):
    if n == 1:
        return ['*']

    stars = starpoint(n//3) 
    result = []  
   
    for i in stars:
        result.append(i * 3)
    for i in stars:
        result.append(i + ' ' * (n // 3) + i)
    for i in stars:
        result.append(i * 3)
    return result

N = int(sys.stdin.readline())
print('\n'.join(starpoint(N)))