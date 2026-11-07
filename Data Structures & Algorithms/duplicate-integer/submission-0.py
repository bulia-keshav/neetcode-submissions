class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        from collections import Counter
        x = Counter(nums)
        for t in x.values():
            if t >1: return True

        return False