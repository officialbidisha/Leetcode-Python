class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.isAnagram("anagram", "nagaram"))  # expect True
    print(sol.isAnagram("rat", "car"))            # expect False
