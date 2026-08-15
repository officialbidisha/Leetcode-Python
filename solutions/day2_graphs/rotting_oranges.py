from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))  # expect 4
    print(sol.orangesRotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]))  # expect -1
    print(sol.orangesRotting([[0, 2]]))  # expect 0
