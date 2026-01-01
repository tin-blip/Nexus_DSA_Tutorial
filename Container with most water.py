class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        currArea = 0

        while left < right:
            if (min(height[left], height[right]) * (right - left) > currArea):
                currArea = min(height[left], height[right]) * (right - left)
            elif(height[left] < height[right]):
                left += 1
            else:
                right -= 1
        return currArea
        
