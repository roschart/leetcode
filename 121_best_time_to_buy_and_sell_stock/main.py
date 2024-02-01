from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return 0


def test(prices: List[int], expected: int) -> bool:
    s = Solution()
    result = s.maxProfit(prices)
    if result != expected:
        raise Exception(f"{result}!={expected}")


if __name__ == "__main__":
    test([7, 1, 5, 3, 6, 4], 5)
