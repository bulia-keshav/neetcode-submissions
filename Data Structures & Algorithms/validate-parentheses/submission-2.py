class Solution:
    def isValid(self, s: str) -> bool:
        st= []
        pairs = {"}" : "{",
        "]":"[",
        ")": "("  }

        for b in s:
            if st and b in pairs:
                if pairs[b] == st[-1]: 
                    st.pop()
                else: 
                    return False
            else: st.append(b)
        return not st




