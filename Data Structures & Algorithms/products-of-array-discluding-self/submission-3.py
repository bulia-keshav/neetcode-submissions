class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        pre = [1]*l
        post = [1]*l
        for i in range(l-1):
            pre[i+1] = pre[i]*nums[i]
        for j in range(l-1,0,-1):
            post[j-1] = post[j]*nums[j]
        return [x*y for x,y in zip(pre,post)]