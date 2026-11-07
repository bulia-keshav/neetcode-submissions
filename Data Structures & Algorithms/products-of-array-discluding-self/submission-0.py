class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if 0 in nums: t = nums.index(0)
        else: t = None
        if t!= None and 0 in nums[t+1: ]:
            return [0]*len(nums)



        elif t != None:
            p =1
            for numb in nums:
                if nums.index(numb) == t: continue
                p *= numb
            lists = [0]*len(nums)
            lists[t] = p
            return lists
            

        else: 
            p = 1
            for numb in nums:
                p *= numb
            return list(map(lambda x: int(p/x), nums))

