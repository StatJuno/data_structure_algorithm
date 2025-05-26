def is_enough(trees, h, m):
    return sum((tree - h) for tree in trees if tree > h) >= m

def find_max_height(trees, m):
    left = 0
    right = max(trees)
    answer = 0

    while left <= right:
        mid = (left + right) // 2
        if is_enough(trees, mid, m):
            answer = mid  # 조건 만족하므로 한 번 더 높여보자
            left = mid + 1
        else:
            right = mid - 1

    return answer

n, m = map(int, input().split())
trees = list(map(int, input().split()))

print(find_max_height(trees, m))