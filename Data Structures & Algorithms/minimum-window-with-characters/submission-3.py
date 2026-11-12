class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from  collections import Counter
        t_c = Counter(t)
        wind = Counter()
        l,r = 0,0
        missing = len(t)                      # CHANGE 1: chars still needed
        res_l, res_r = 0, len(s) + 1          # CHANGE 4: store indices, not strings
        if len(s) <  len(t) : return ""
        while r < len(s) or missing == 0:     # CHANGE 3: was `not t_c - wind`

            if missing > 0:                   # CHANGE 3: was `t_c - wind`
                if s[r] in t_c:
                    wind[s[r]] += 1
                    if wind[s[r]] <= t_c[s[r]]:   # CHANGE 2: this copy was actually needed
                        missing -= 1
                r+=1
                
            if missing == 0:                  # CHANGE 3: was `not t_c - wind`
                if r - l < res_r - res_l:     # CHANGE 4: compare lengths with math
                    res_l, res_r = l, r
                if s[l] in t_c:
                    wind[s[l]] -=1
                    if wind[s[l]] < t_c[s[l]]:    # CHANGE 2: we just lost a needed char
                        missing += 1
                l +=1
        return "" if res_r > len(s) else s[res_l:res_r]   # CHANGE 4: slice once at the end