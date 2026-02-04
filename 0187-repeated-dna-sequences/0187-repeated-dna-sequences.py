class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        res = set()
        seqmap = set()
        if n <= 10:
            return []
        for i in range(n-10+1):
            seq = s[i:i + 10]
            if seq in res:
                continue
            if seq in seqmap:
                res.add(seq)
            else:
                seqmap.add(seq)
        return list(res)