from __future__ import annotations

from typing import TypeVar, Generic, Callable

T = TypeVar("T")
U = TypeVar("U")

class SegmentTree(Generic[T, U]):
    def __init__(self, size: int, function: Callable[[U, U], U], default: U):
        self.size = size
        self.tree = [default] * (2 * size)
        self.function = function
        self.default = default

    def change(self, target: int, diff: U, idx: int, start: int, end: int):
        if end < target or target < start:
            return
        
        self.tree[idx] += diff
        if start != end:
            mid = (start + end) // 2
            self.change(target, diff, 2 * idx, start, mid)
            self.change(target, diff, 2 * idx + 1, mid + 1, end)

    def print_sum(self, count: int, idx: int, start: int, end: int) -> int:
        if start == end:  # 리프노드 도달
            return start
        
        mid = (start + end) // 2
        if self.tree[2 * idx] >= count:
            return self.print_sum(count, 2 * idx, start, mid)
        else:
            return self.print_sum(count - self.tree[2 * idx], 2 * idx + 1, mid + 1, end)

import sys

"""
TODO:
- 일단 SegmentTree부터 구현하기
- main 구현하기
"""

def main() -> None:
    input = sys.stdin.read().strip()
    if not input:
        return
    
    data = input.split()
    idx = 0

    n = int(data[idx])
    idx += 1

    MAX_TASTE = 1000000
    tree_size = 2**21

    # Segment Tree for counting candies
    seg_tree = SegmentTree(tree_size, lambda x, y: x + y, 0)
    
    results = []

    for _ in range(n):
        A = int(data[idx])
        B = int(data[idx + 1])

        if A == 1:
            # Find the B-th most delicious candy
            taste_index = seg_tree.print_sum(B, 1, 1, MAX_TASTE)
            results.append(taste_index)
            # Remove that candy by decrementing the count
            seg_tree.change(taste_index, -1, 1, 1, MAX_TASTE)
            idx += 2
        elif A == 2:
            # Update the segment tree with candy addition/removal
            C = int(data[idx + 2])
            seg_tree.change(B, C, 1, 1, MAX_TASTE)
            idx += 3

    for result in results:
        print(result)

if __name__ == "__main__":
    main()
