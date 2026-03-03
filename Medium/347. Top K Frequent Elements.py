class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        d1 = defaultdict(list)
        ans = []
        for i in nums:
            d[i] += 1
        for value, freq in d.items():
            d1[freq].append(value)
        for f in range(len(nums), -1, -1):
            if f in d1:
                for i in d1[f]:
                    if k > 0:
                        ans.append(i)
                        k -= 1
        return ans
    
# Create a dictionary for both, initially creating frequencies, then based on frequencies, then loop