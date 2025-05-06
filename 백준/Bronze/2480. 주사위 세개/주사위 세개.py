x, y, z = map(int, input().split())

if x == y == z:
    print(10000 + x*1000)
elif x == y or y==z or z == x:
    print(1000 + x*100) if x == y else print(1000 + z*100)
else:
    print(max(x,y,z) * 100)