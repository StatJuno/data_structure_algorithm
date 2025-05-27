import sys
input = sys.stdin.readline
N = int(input())
meetings = []

for i in range(N):
    start, end = map(int, input().split())
    meetings.append((end, start))
    
meetings.sort()

count = 0
current_end_time = 0

for end, start in meetings:
    if start >= current_end_time:
        count += 1
        current_end_time = end

print(count)