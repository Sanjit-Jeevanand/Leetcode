class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        ans = []
        nums = sorted(nums)
        n = len(nums)
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = n - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s > 0:
                    r -= 1
                elif s < 0:
                    l += 1
                if s == 0:
                    ans.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
        return ans
    
# Sorting + 2 Pointer on rest

# Template: 
    # sort nums

    # for each i:
    #     skip duplicate i

    #     l = i+1
    #     r = end

    #     while l < r:
    #         compute sum

    #         move pointers based on sum

    #         if sum == 0:
    #             record triplet
    #             move both pointers
    #             skip duplicates