import sys
input = sys.stdin.readline
N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

white, blue = 0, 0

def divide_conquer(x, y, size):
    global white, blue
    color = paper[x][y]
    is_same = True
    
    for i in range(x, x+size):
        for j in range(y, y+size):
            if paper[i][j] != color:
                is_same = False
                break
        if not is_same:
            break
            
    if is_same:
        if color == 0:
            white += 1
        else:
            blue += 1
    else:
        new_size = size // 2
        divide_conquer(x, y, new_size)
        divide_conquer(x + new_size, y, new_size)
        divide_conquer(x, y + new_size, new_size)
        divide_conquer(x + new_size, y + new_size, new_size)
        
        
divide_conquer(0, 0, N)
print(white)
print(blue)