class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = set()

        def recurse(open, close, curr):
            if open == 0 and close == 0:
                res.add(curr[:])
                return
            
            if open >= 0:
                recurse(open-1, close, curr + '(')
            
                if close > 0 and close - open > 0:
                    recurse(open, close-1, curr + ')')

            return
        
        recurse(n, n, '')
        return list(res)


