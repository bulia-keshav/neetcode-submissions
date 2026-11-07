class Solution:
    def maxArea(self, heights: List[int]) -> int:
        lo, hi = 0, len(heights)-1
        max_area = 0
        while lo<hi:
            hlo =heights[lo]
            hhi =heights[hi]
            area = (hi-lo)*(min(hlo,hhi))
            if area > max_area: max_area=area

            if hlo>hhi: hi -=1
            else:  lo +=1
        return max_area    