from typing import List


class Solution:
    def removeDuplicates(self,  nums: List[int]) -> int:
        match nums:
            case []:
                return 0
            case [_]:
                return 1
            case [elem1,  elem2]:
                if elem1 == elem2:
                    return 1
                else:
                    return 2
            case _:
                slow = 0
                fast = 1
                while fast < len(nums):
                    if nums[slow] == nums[fast]:
                        fast += 1
                    else:
                        slow += 1
                        nums[slow] = nums[fast]
                        fast += 1
                return slow+1


if __name__ == "__main__":
    s = Solution()
    nums = [1,  1,  2]
    k = s.removeDuplicates(nums)
    print(k,  nums)

    nums = [1,  1,  1]
    k = s.removeDuplicates(nums)
    print(k,  nums)

    nums = [0,  0,  1,  1,  1,  2,  2,  3,  3,  4]
    k = s.removeDuplicates(nums)
    print(k,  nums)
