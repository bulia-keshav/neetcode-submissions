
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from  collections import  Counter
        cs1 = Counter(s1)
        i,j = 0, len(s1)
        cs2 = Counter(s2[i:j])
        while j<= len(s2):
            if cs1 == cs2: return True
            try :cs2[s2[j]] +=1
            except: return False
            cs2[s2[i]] -=1
            i+=1
            j+=1

        return False
