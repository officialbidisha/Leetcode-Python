from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.containsNearbyDuplicate([1, 2, 3, 1], 3))     # expect True
    print(sol.containsNearbyDuplicate([1, 0, 1, 1], 1))     # expect True
    print(sol.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))  # expect False
