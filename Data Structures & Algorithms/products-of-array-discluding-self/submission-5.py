class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        if nums.count(0 )>1: return [0]*l

        res = [1]*l
        post = 1
        for i in range(l-1):
            res[i+1] = res[i]*nums[i]
        for j in range(l-1,0,-1):
            post *=nums[j]
            res[j-1] = post*res[j-1]

        return res