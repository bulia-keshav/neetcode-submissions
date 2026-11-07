class Solution:

    def encode(self, strs: List[str]) -> str:   
        t = ""
        for word in strs:
            word = str(len(word)) + "#" + word    
            t +=word
        return t
    def decode(self, s: str) -> List[str]:
        i = 0
        l = [] 
        while i <len(s):
            findhash = s.find("#", i)
            findnumber = int(s[i: findhash])
            l.append(s[findhash + 1: findhash+ 1+findnumber])
            i = findhash+ 1+findnumber
        return l