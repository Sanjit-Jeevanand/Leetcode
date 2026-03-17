class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        s = []
        area = 0
        heights.append(0)
        for i in range(len(heights)):
            while s and heights[i] < heights[s[-1]]:
                h = heights[s.pop()]
                if s:
                    width = i - s[-1] - 1
                else:
                    width = i
                area = max(area, h * width)
            s.append(i)
        return area
    
# Maintain a stack of indices; if a smaller element appears; resolve all larger elemets