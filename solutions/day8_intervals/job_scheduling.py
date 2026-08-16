"""
Maximum Profit in Job Scheduling — LC 1235.

You have `n` jobs, each with a startTime[i], endTime[i], profit[i]. You're
given three arrays of length n. Find the maximum profit you can take such
that no two chosen jobs overlap in time (a job with endTime == another
job's startTime does NOT overlap — they can both be taken).

You can't do part of a job — take it entirely or not at all.

A frequently-reported interview classic. Pattern: DP + binary search on intervals.
"""

import bisect
from typing import List


class Solution:
    def jobScheduling(
        self, startTime: List[int], endTime: List[int], profit: List[int]
    ) -> int:
        """Top-down: memoized take/skip over jobs sorted by start time."""
        intervals = sorted(zip(startTime, endTime, profit))
        cache = {}

        def dfs(i):
            if i == len(intervals):
                return 0
            if i in cache:
                return cache[i]

            # don't include
            res = dfs(i + 1)

            # include: jump to the first job that starts at or after this end.
            # bisect_left == "first element >= probe". (-1, -1) is a sentinel
            # below any real (end, profit), so (end, -1, -1) sorts before every
            # job whose start == our end, and we land ON that first job.
            j = bisect.bisect_left(intervals, (intervals[i][1], -1, -1))
            cache[i] = res = max(res, intervals[i][2] + dfs(j))
            return res

        return dfs(0)


class SolutionIterative:
    def jobScheduling(
        self, startTime: List[int], endTime: List[int], profit: List[int]
    ) -> int:
        """Same DP bottom-up — no recursion limit, and the bisect is explicit."""
        intervals = sorted(zip(startTime, endTime, profit))
        starts = [s for s, _, _ in intervals]  # sorted, so bisect-able on its own
        n = len(intervals)

        # dp[i] = best profit obtainable using jobs i..n-1
        dp = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            _, end, p = intervals[i]
            j = bisect.bisect_left(starts, end)  # first job starting >= end
            dp[i] = max(dp[i + 1], p + dp[j])
        return dp[0]


if __name__ == "__main__":
    sol = Solution()

    print(sol.jobScheduling([1, 2, 3, 3], [3, 4, 5, 6], [50, 10, 40, 70]))
    # expect 120  (job0 [1,3]=50 + job3 [3,6]=70)

    print(sol.jobScheduling([1, 2, 3, 4, 6], [3, 5, 10, 6, 9], [20, 20, 100, 70, 60]))
    # expect 150  (job0 [1,3]=20 + job3 [4,6]=70 + job4 [6,9]=60)

    print(sol.jobScheduling([1, 1, 1], [2, 3, 4], [5, 6, 4]))
    # expect 6  (best single job: profit 6)

    it = SolutionIterative()
    print(it.jobScheduling([1, 2, 3, 3], [3, 4, 5, 6], [50, 10, 40, 70]))  # 120
    print(
        it.jobScheduling([1, 2, 3, 4, 6], [3, 5, 10, 6, 9], [20, 20, 100, 70, 60])
    )  # 150
    print(it.jobScheduling([1, 1, 1], [2, 3, 4], [5, 6, 4]))  # 6
