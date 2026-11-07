class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i,j = 0,0
        lent = 0
        max_len = 0

        exis = {}
        while i<=j and j < len(s):
            if s[j] not in exis:
                exis[s[j]] = j
                lent = j-i +1
                j+=1
                
                max_len = max(max_len, lent)
                continue
            i = max(i, exis[s[j]] + 1)
            max_len = max(max_len, j-i+1)

            exis[s[j]] = j
            j+=1

                    

        return max_len 
