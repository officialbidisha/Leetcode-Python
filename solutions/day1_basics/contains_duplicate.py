class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        map = {}
        for i in range(len(nums)):
            if map.get(nums[i]) == 1 :
               return True
            map[nums[i]] = map.get(nums[i], 0) + 1
        return False