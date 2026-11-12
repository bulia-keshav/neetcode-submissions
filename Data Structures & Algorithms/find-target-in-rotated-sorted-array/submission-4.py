class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums) -1
        temp = -1
        while l <=r:
            mid = (l+r)//2

            if nums[mid] <= nums[-1]:
                temp = mid
                r = mid -1
            else:
                l = mid +1
        output = -1
        if target >= nums[0]: 
            l,r = 0, temp
        if target <= nums[-1]:
            l,r =   temp, len(nums)-1
        while l <=r:
            mid = (l+r)//2    
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid -1
            else: l = mid +1
        return output