class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter

        s_t = sorted(Counter(nums).items(), key = lambda x: x[1], reverse =True)
        return list(map(lambda x: x[0], s_t))[0:k]
