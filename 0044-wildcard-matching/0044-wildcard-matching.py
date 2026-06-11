class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n1 = len(s)
        sub = []
        st = []
        for x in p:
            if st and st[-1] == '*' and x == '*':
                continue
            else:
                st.append(x)
                sub.append(x)
        
        p = ''.join(sub)
        n2 = len(p)
        print(p)
        if n1 == 0 and n2 == 1 and p[0] == '*':
            return True


        @cache
        def dp(i, j):
            if j == n2:
                return i == n1
            
            if i == n1:
                return all(x == '*' for x in p[j:])
            
            if p[j] == '*':
                return dp(i+1, j) or dp(i+1, j+1) or dp(i, j+1)
            
            if p[j] == '?':
                return dp(i+1, j+1)
            
            if s[i] == p[j]:
                return dp(i+1, j+1)
            
            if s[i] != p[j]:
                return False
        
        return dp(0, 0)