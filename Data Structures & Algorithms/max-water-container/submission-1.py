class Solution:
    def maxArea(self, heights: List[int]) -> int:
        lo, hi = 0, len(heights)-1
        max_area = 0
        while lo<hi:
            hlo =heights[lo]
            hhi =heights[hi]
            max_area = max(max_area,(hi-lo)*(min(hlo,hhi)))

            if hlo>hhi: hi -=1
            else:  lo +=1
        return max_area    