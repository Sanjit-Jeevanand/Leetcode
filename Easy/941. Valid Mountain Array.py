class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        rev = False
        n = len(arr)
        if n < 3 : return False
        for i in range(1,n):
            if arr[i] <= arr[i-1]:
                break
        if i == 1 or i == n: return False
        for x in range(i,n):
            if arr[x] >= arr[x-1]:
                return False
        return True