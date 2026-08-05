class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        map = {}
        for i in range(len(nums)):
            map[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if(map.get(complement)) and map.get(complement)!= i:
                return [map.get(complement), i]
        return []