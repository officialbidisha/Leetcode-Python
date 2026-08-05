from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.productExceptSelf([1, 2, 3, 4]))    # expect [24, 12, 8, 6]
    print(sol.productExceptSelf([-1, 1, 0, -3, 3]))  # expect [0, 0, 9, 0, 0]
