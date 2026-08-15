"""
Each listing has availability given as a sorted list of day integers.
Given an inclusive requested range [S, E], return every unordered pair of
listings (X, Y) such that there exists a split point T, S <= T < E, where
X covers S..T consecutively and Y covers T+1..E consecutively.

Return each pair once. Aim for better than O(L^2 * R) where L = number of
listings, R = range length.

Edge cases to think about: missing boundary days; both listings covering
the whole range; identical availability; no valid pair; S == E.
"""

from bisect import bisect_right
from typing import List, Tuple


class Solution:
    def splitStayPairs(
        self, listings: List[List[int]], s: int, e: int
    ) -> List[Tuple[int, int]]:
        # S == E means the valid split-point range S <= T < E is empty --
        # no integer T can be both >= S and < S. No pair is ever possible.
        if s == e:
            return []

        # prefix_candidates[i] = (furthest day listing i can cover as the
        # FIRST half, starting from S with no gaps). Only listings that
        # contain S qualify.
        prefix_candidates = []
        # suffix_candidates[i] = (earliest day listing i can cover as the
        # SECOND half, ending at E with no gaps). Only listings that
        # contain E qualify.
        suffix_candidates = []

        for listing_id, availability in enumerate(listings):
            if s in availability:
                day_index = availability.index(s)
                # Walk forward only while the next day keeps the run
                # unbroken and stays within E -- checking before committing
                # means availability[day_index] is always valid, however
                # the loop stops.
                while (
                    day_index + 1 < len(availability)
                    and availability[day_index + 1] - availability[day_index] == 1
                    and availability[day_index + 1] <= e
                ):
                    day_index += 1
                prefix_reach_day = availability[day_index]
                prefix_candidates.append((prefix_reach_day, listing_id))

            if e in availability:
                day_index = availability.index(e)
                # Mirror image: walk backward while the previous day keeps
                # the run unbroken and stays within S.
                while (
                    day_index - 1 >= 0
                    and availability[day_index] - availability[day_index - 1] == 1
                    and availability[day_index - 1] >= s
                ):
                    day_index -= 1
                suffix_start_day = availability[day_index]
                suffix_candidates.append((suffix_start_day, listing_id))

        # Sort by day so we can binary-search "which suffixes qualify"
        # instead of comparing every prefix against every suffix.
        suffix_candidates.sort()
        suffix_start_days = [day for day, _ in suffix_candidates]
        suffix_listing_ids = [listing_id for _, listing_id in suffix_candidates]

        valid_pairs = set()
        for prefix_reach_day, prefix_listing_id in prefix_candidates:
            # A suffix listing qualifies as a partner when its suffix starts
            # at most one day after this prefix's reach ends (no gap).
            max_allowed_suffix_start = prefix_reach_day + 1
            cutoff_index = bisect_right(suffix_start_days, max_allowed_suffix_start)
            for suffix_listing_id in suffix_listing_ids[:cutoff_index]:
                if suffix_listing_id != prefix_listing_id:
                    # Store pairs in canonical (min, max) order so a listing
                    # that covers the whole range (appearing in both
                    # prefix_candidates and suffix_candidates) doesn't
                    # produce both (X, Y) and (Y, X) for the same
                    # unordered pair.
                    pair = (
                        min(prefix_listing_id, suffix_listing_id),
                        max(prefix_listing_id, suffix_listing_id),
                    )
                    valid_pairs.add(pair)

        return list(valid_pairs)


if __name__ == "__main__":
    sol = Solution()

    a = [1, 2, 3, 6, 7, 10, 11]
    b = [3, 4, 5, 6, 8, 9, 10, 13]
    c = [7, 8, 9, 10, 11]

    print(sol.splitStayPairs([a, b, c], 3, 11))  # expect [(1, 2)]

    # no valid pair
    print(sol.splitStayPairs([[1, 2], [5, 6]], 1, 6))  # expect []

    # both listings cover the whole range -- one pair, not two
    whole = [3, 4, 5, 6, 7, 8, 9, 10, 11]
    print(sol.splitStayPairs([whole, list(whole)], 3, 11))  # expect [(0, 1)]

    # identical availability, doesn't cover the full range
    same = [3, 4, 5]
    print(sol.splitStayPairs([same, list(same)], 3, 11))  # expect []

    # S == E: no split point can ever exist
    print(sol.splitStayPairs([a, b, c], 5, 5))  # expect []
