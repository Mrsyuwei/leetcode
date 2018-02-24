# -*- coding: UTF-8 -*-


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        areaList=[]
        i=0
        j=len(height)-1
        while i < j:
            x=j-i
            y=min(height[i],height[j])
            area=x*y
            areaList.append(area)
            if y==height[i]:
                i=i+1
            else:
                j=j-1
        return max(areaList)

height=[2,6,8,3,5]
p=Solution()
print p.maxArea(height)
