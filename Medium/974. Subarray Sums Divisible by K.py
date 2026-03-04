class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        d = defaultdict(int)
        d[0] = 1
        count,psum = 0,0
        for i in range(len(nums)):
            psum += nums[i]
            if psum % k in d:
                count += d[psum%k]
            d[psum%k] += 1
        return count
    
# Store frequency of psum%k
# Prefix + Hashmap + Frequecy Counting