class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo,hi =  0, len(nums) -1
        result = -1

        while lo <= hi:
            mid = (lo + hi)//2
            midn = nums[mid]
            if midn == target:
                result = mid
                hi = mid- 1
            elif midn> target:
                hi = mid -1
            else:
                lo = mid +1 
        return result                