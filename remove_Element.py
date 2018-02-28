# -*- coding: UTF-8 -*-
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if len(nums)==0:
            return len(nums)
        else:
            while val in nums:
                index_nums = nums.index(val)
                nums.pop(index_nums)
            return len(nums)

nums=[1,1,2,3,1,1]
val=1
p=Solution()
print p.removeElement(nums,val)