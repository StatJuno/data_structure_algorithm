# 입력
import sys
N = int(sys.stdin.readline())
nums = [int(sys.stdin.readline()) for _ in range(N)]

# 산술평균
mean = round(sum(nums) / N)

# 중앙값
nums.sort()
median = nums[N // 2]

# 최빈값
from collections import Counter 
freq = Counter(nums)
mode_list = freq.most_common()  # 빈도순 정렬
max_freq = mode_list[0][1]

# 최빈값 중 가장 빈도가 높은 값들 추리기
modes = [num for num, cnt in mode_list if cnt == max_freq]
modes.sort()
mode = modes[0] if len(modes) == 1 else modes[1]  # 두 번째로 작은 값

# 범위
range_val = max(nums) - min(nums)

print(mean)
print(median)
print(mode)
print(range_val)