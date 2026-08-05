from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.singleNumber([2, 2, 1]))         # expect 1
    print(sol.singleNumber([4, 1, 2, 1, 2]))   # expect 4
