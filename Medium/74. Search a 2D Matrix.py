class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        row = 0
        l, r = 0, m-1
        while l <= r:
            mid = (l+r)//2
            if matrix[mid][n-1] < target:
                l = mid+1
            elif matrix[mid][0] > target:
                r = mid - 1
            else:
                row = mid   
                break  
        l,r = 0, n-1
        while l <= r:
            mid = (l+r)//2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False

# Two Binary Searches; Make sure to break and the 0 and n-1 criteria in row search