from collections import Counter
from typing import List


class solutionC:
    def removeDuplicates(self, nums: List[int]) -> int:
        ocurrences = 1
        fast = 1
        slow = 1

        for fast in range(1, len(nums)):
            if nums[fast] == nums[fast-1]:
                ocurrences += 1
            else:
                ocurrences = 1

            if ocurrences <= 2:
                nums[slow] = nums[fast]
                slow += 1
        return slow


class SolutionA:
    def removeDuplicates(self, nums: List[int]) -> int:
        c = Counter(nums)
        d = {k: min(v, 2) for k, v in c.items()}
        result = sum(d.values())
        nums[:result] = [k for k, v in d.items() for _ in range(v)]
        return result


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 0
        fast = 1
        result = 1
        occurences = 1
        while fast < len(nums):
            if nums[slow] == nums[fast]:
                occurences += 1
                if occurences <= 2:
                    slow += 1
                    fast += 1
                    result += 1
                else:
                    fast += 1
            else:
                result += 1
                k = fast-slow-1
                i = 0
                while i < k and fast+i < len(nums):
                    nums[slow+i+1] = nums[fast+i]
                    i = i+1
                slow += 1
                fast = fast+1
                occurences = 1
        return result


if __name__ == "__main__":
    sa = SolutionA()
    s = Solution()
    sc = solutionC()

    nums = [1, 1, 1, 2, 2, 3]
    numsA = nums[:]
    numsC = nums[:]
    c = sc.removeDuplicates(numsC)
    r = s.removeDuplicates(nums)
    e = sa.removeDuplicates(numsA)
    print(nums, numsA, r, e)
    assert (numsA == nums == numsC)
    assert (r == e == c)

    nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    numsA = nums[:]
    numsC = nums[:]
    c = sc.removeDuplicates(numsC)
    r = s.removeDuplicates(nums)
    e = sa.removeDuplicates(numsA)
    print(nums, numsA, r, e)
    assert (numsA == nums == numsC)
    assert (r == e == c)

    nums = [1, 1]
    numsA = nums[:]
    numsC = nums[:]
    c = sc.removeDuplicates(numsC)
    r = s.removeDuplicates(nums)
    e = sa.removeDuplicates(numsA)
    print(nums, numsA, r, e)
    assert (numsA == nums == numsC)
    assert (r == e == c)
