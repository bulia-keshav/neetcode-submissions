class Solution:
    def findMin(self, nums: List[int]) -> int:
        result = -1
        l,r  = 0, len(nums) - 1
        while l <= r:
            mid = (l+r)//2
            if nums[mid] <= nums[-1]: 
                r = mid -1
                result = nums[mid]
            else:
                l = mid +1 
        return result