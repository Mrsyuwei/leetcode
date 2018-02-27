# -*- coding: UTF-8 -*-
import json

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            length=0
            return length
        else:
            i=nums[0]
            j=1
            while j<len(nums):
                if i==nums[j]:
                    nums.pop(j)
                else:
                    i=nums[j]
                    j=j+1
            length=len(nums)
            return length

nums=[]
p=Solution()
print p.removeDuplicates(nums)