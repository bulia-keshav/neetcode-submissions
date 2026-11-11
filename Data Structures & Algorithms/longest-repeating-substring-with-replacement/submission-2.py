class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,r = 0,0
        res = 0
        count = {}

        while r < len(s):

            count[s[r]] = count.get(s[r],0) + 1

            if (r-l +1) - max(count.values()) > k:
                count[s[l]] -=1
                l+=1

            res = max(r-l+1,res)
            r+=1
        return res