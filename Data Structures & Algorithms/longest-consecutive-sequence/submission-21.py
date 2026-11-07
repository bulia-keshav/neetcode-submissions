class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []: return 0
        sets = set(nums)
        i =1
        highest =1

        for numb in nums:
            i = 1
            if numb-1 in sets: continue
            while True:
                if numb + 1 in sets: 
                    i += 1
                    numb += 1

                else: break
            if i > highest: 
                highest = i    
               

        return highest