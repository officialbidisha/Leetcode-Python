from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        buckets= []
        for num in nums:
            freq[num] = freq.get(num, 0) + 1 # 2-> 1 (2 is present once)
        for i in range(len(nums)+1):
            buckets.append([])
        for key,value in freq.items():
            buckets[value].append(key)
        res = []
        # traverse the array from the end
        #start, stop, step
        for count in range(len(nums), 0, -1):
            for num in buckets[count]:
                res.append(num)
                if len(res) == k:
                    return res
        return res
        


if __name__ == "__main__":
    sol = Solution()
    print(sol.topKFrequent([1, 1, 1, 2, 2, 3], 2))  # expect [1, 2]
