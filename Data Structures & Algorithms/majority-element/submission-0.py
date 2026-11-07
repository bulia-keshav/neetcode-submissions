class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import Counter
        freq  = Counter(nums)

        return max(freq, key = lambda x: freq[x])