class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        lb = 0
        ub = len(heights) - 1

        while lb < ub:
            area = min(heights[lb], heights[ub]) * (ub - lb)
            if area >= maxArea:
                maxArea =  area
            if heights[lb] <= heights[ub]:
                lb += 1
            else:
                ub -= 1
        
        return maxArea