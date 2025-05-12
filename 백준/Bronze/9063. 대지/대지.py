N = int(input())
x_points = []
y_points = []
for i in range(N):
    x, y = map(int, input().split())
    x_points.append(x)
    y_points.append(y)

print((max(x_points) - min(x_points)) * (max(y_points) - min(y_points)))