# -*- coding: UTF-8 -*-
# roman to integer range for 1-3999
# 1 - 8:I, V
# 9 - 89:I, V, X, L
# 90 - 899:I, V, X, L, C, D
# 900 - 3999:I, V, X, L, C, D, M,


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        Dict = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }

        num=0
        last_num=Dict[s[0]]
        for i in s:
            if len(s)==1:
                num=Dict[i]
            elif last_num<Dict[i]:
                num=num-2*last_num+Dict[i]
            else:
                num=num+Dict[i]
            last_num=Dict[i]
        return num






s = 'VIII'
p = Solution()
print p.romanToInt(s)
