class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sums = 0
        max_sum = nums[0]
        for num in nums:
            sums +=num
            max_sum = max(max_sum,sums)
            if  sums <0:
                sums = 0



        return max_sum