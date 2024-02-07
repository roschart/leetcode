from typing import List
import unittest


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        match prices:
            case []:
                return 0
            case _:
                result = 0
                mini = prices[0]
                for i in range(1, len(prices)):
                    v = prices[i]
                    mini = min(v, mini)
                    result = max(result, v - mini)
                return result


class TestSolution(unittest.TestCase):
    def test_maxProfit(self):
        s = Solution()
        # Aquí se definen los casos de prueba como tuplas de (entrada, salida esperada)
        test_cases = [
            ([7, 1, 5, 3, 6, 4], 5),
            ([7, 6, 4, 3, 1], 0),
            ([], 0)
            # Puedes agregar más casos de prueba según sea necesario
        ]

        for prices, expected in test_cases:
            with self.subTest(prices=prices, expected=expected):
                self.assertEqual(s.maxProfit(prices), expected,
                                 f"Failed for prices: {prices}")


if __name__ == "__main__":
    unittest.main()
