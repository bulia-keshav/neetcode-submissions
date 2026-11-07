class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ss = {}

        if len(s) != len(t): return False
        for x in s:
            ss[x] = ss.get(x, 0) + 1

        for x in t:
            if x not in ss:
                return False
            ss[x] -= 1
            if ss[x] < 0:
                return False
            
        return True