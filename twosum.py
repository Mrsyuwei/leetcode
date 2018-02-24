# -*- coding: UTF-8 -*-


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 方案一
        indices = []
        sortnums = sorted(nums)
        i = 0
        j = len(sortnums)-1
        sum = sortnums[i] + sortnums[j]
        while sum != target:
            if sum > target:
                j = j - 1
            else:
                i = i + 1
            if i==j:
                print "None"
                exit(1)
            sum = sortnums[i] + sortnums[j]
        for list in range(len(nums)):
            if (sortnums[i]==nums[list] or sortnums[j]==nums[list]):
                indices.append(list)
        return indices
        #
        # indices=[]
        # for i in range(len(nums)):
        #     sub=target-nums[i]
        #     if sub in nums and nums.index(sub)!=i:
        #         indices.append(i)
        #         indices.append(nums.index(sub))
        #         break
        # return indices

nums = [7, 2, 11, 15, 8,2]
target = 4
P = Solution()
print P.twoSum(nums, target)
