class Solution:
    def isPalindrome(self, s: str) -> bool:

        c= ""
        for char in s:
            if char.isalnum():
                c += char.lower()
        lo, hi = 0 , len(c) -1
        while lo < hi:
            if c[lo] != c[hi]:
                return False
            lo +=1
            hi -=1
        return True

           