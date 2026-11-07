class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import Counter
        l = {}
        for w in strs:
            tsw = tuple(sorted(w))
            if tsw not in l: l[tsw] = [w]
            else: l[tsw].append(w)
        return list(l.values())

        



            


