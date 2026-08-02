class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        largestArea = 0

        while l < r:
            area = min(heights[l], heights[r]) * (r - l)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

            if area > largestArea:
                largestArea = area
            
        return largestArea
            
