class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen = set()
        for i in range(len(nums)):
            if map.get(nums[i]) in seen :
               return True
            seen.add(nums[i])
        return False