class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1

        while lo <= hi:
            mid = (lo + hi)//2
            midn = nums[mid]

            if midn == target:
                if nums[mid - 1] == target and len(nums) != 1:
                    hi = mid - 1
                else: return mid


            if midn < target:
                lo = mid+1
            elif midn > target:
                hi = mid-1    
        return -1         


