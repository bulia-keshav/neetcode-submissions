class Solution:
    def isValid(self, s: str) -> bool:
        st= []
        pairs = {"}" : "{",
        "]":"[",
        ")": "("  }

        for b in s:
            if len(st) < 1: 
                st.append(b)
                continue
            if pairs.get(b, None) == st[-1]: st.pop()
            else: st.append(b)        
        return len(st) == 0