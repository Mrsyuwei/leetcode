# -*- coding: UTF-8 -*-


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        arealist = []
        i = 0
        j = len(height) - 1
        while i < j:
            x = j - i
            y = min(height[i], height[j])
            area = x * y
            arealist.append(area)
            if y == height[i]:
                i = i + 1
            else:
                j = j - 1
        return max(arealist)


height = [2, 6, 8, 3, 5]
p = Solution()
print p.maxArea(height)
