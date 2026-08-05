from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Time Complexity : O(m)
        res = {}
        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord('a')]= (count[ord(char) - ord('a')] or 0) + 1
            # count is a list, and lists are mutable so they can't be dict keys.
            # tuple(count) converts it to an immutable, hashable fingerprint —
            # anagrams produce identical counts, so they land on the same key.
            # Alternative: key = "".join(sorted(word)) — simpler, O(k log k)
            # instead of O(k), no tuple conversion needed since strings are
            # already hashable.
            key = tuple(count)
            if key not in res:
                res[key] = []
            res[key].append(word)
        return list(res.values())


if __name__ == "__main__":
    sol = Solution()
    print(sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    # expect groups like [["eat","tea","ate"],["tan","nat"],["bat"]] (any order)
