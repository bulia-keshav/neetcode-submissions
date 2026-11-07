class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        t = Counter(nums)
        a = []
        if not nums: return []
        for _ in range(k):
            maxima = max(t.items(), key = lambda x: x[1])[0]
            t.pop(maxima)
            a.append(maxima)
        return a
