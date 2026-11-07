class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ss = {}
        tt = {}
        sets = set(s)
        sett = set(t)
        for x in sets:
            ss[x] = s.count(x)
        for y in sett:
            tt[y] = t.count(y)

        return ss ==tt   