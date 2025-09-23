class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        V1=version1.split('.')
        V2=version2.split('.')
        n1, n2=len(V1), len(V2)
        for x1, x2 in zip(V1, V2):
            if int(x1)<int(x2): return -1
            if int(x1)>int(x2): return 1
        n3=min(n1, n2)
        if n1<n2: 
            return -1 if any(int(V2[i])>0 for i in range(n3, n2)) else 0
        elif n1>n2:
            return 1 if any(int(V1[i])>0 for i in range(n3, n1)) else 0
        return 0