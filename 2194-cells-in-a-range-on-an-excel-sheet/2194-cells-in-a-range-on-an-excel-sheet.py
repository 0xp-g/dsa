class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        a1 = int(ord(s[0]))
        a2 = int(ord(s[3]))
        n1 = int(s[1])
        n2 = int(s[4])
        res = []
        print(a1, a2, n1, n2)
        for i in range(a2-a1+1):
            for j in range(n1, n2+1):
                res.append(chr(i+a1)+str(j))
        return res