# -*- coding: UTF-8 -*-

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            return nums.index(target)
        else:
            i=0
            while i<len(nums) and nums[i]<target:
                i=i+1
            # nums.append(i-1,target)
            return i


nums=[1,2,3,4,6,7]
target=8
p=Solution()
print p.searchInsert(nums,target)
