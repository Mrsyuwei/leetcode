# -*- coding: UTF-8 -*-

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n==1:
            first='1'
        else:
            for i in range(n):
                if i==0:
                    first='1'
                else:
                    first=self.Single(first)
        return first
    def Single(self,first):
        sum = 0
        sum_num = first[0]
        new_num = ''
        for j in range(len(first)):
            if sum_num == first[j]:
                sum = sum + 1
            else:
                new_num = new_num + str(sum) + first[j - 1]
                sum_num = first[j]
                sum = 1
        new_num = new_num + str(sum) + first[j]
        return new_num


n=4
p=Solution()
print p.countAndSay(n)