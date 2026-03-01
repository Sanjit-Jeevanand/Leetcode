class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = 0
        psum = 0
        if n <= 1:
            return int(nums[0] == k)
        d = {0 : 1}
        for i in range(n):
            psum += nums[i]
            if psum - k in d:
                count += d[psum - k]
            d[psum] = d.get(psum, 0) + 1
        return count
        
# Patten combination : Prefix Sum + Hashmap Lookup of Complement
# psum - k in dictionary; that is the check