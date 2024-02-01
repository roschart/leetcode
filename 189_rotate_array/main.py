
from collections import deque
from typing import List


class SolutionA:
    def rotate(self, nums: List[int], k: int) -> None:
        d = deque(nums)
        d.rotate(k)
        data[:] = list(d)


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        d = deque(nums)
        d.rotate(k)
        print(d)
        stack = nums[-k:]
        print(stack)
        n=len(nums)
        for i in range(k, -1, -1):
            print(i, nums[i])
            nums[]


s = Solution()
data = [1, 2, 3, 4, 5, 6, 7]

s.rotate(data, 3)

print(data)
