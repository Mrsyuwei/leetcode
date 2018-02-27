# -*- coding: UTF-8 -*-

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        #方案一
        # j = 1
        # if len(strs) == 0:
        #     pattern = ''
        # else:
        #     pattern = strs[0]
        # while j < len(strs):
        #     while strs[j].startswith(pattern) == False:
        #         pattern = pattern[0:len(pattern) - 1]
        #     j = j + 1
        # return pattern
        strs_sort=sorted(strs,key=lambda s:len(s))
        if len(strs)==0:
            pattern=''
        else:
            pattern=strs_sort[0]
        for j in strs_sort[1:len(strs_sort)]:
            while j.startswith(pattern)==False:
                pattern=pattern[0:len(pattern)-1]
                continue
        return pattern


strs = ['abcd', 'abe', 'abc', 'aba', 'abcedf']
p = Solution()
print p.longestCommonPrefix(strs)
