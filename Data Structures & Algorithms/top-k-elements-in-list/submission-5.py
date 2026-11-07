class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        t= sorted(list(Counter(nums).items()), key = lambda x: x[1], reverse= True)
        return [num for num, count in t[:k]]