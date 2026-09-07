class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        ds = DSU(n)
        email_map = {}
        mails = defaultdict(list)
        ls = []

        for i in range(n):
            for mail in accounts[i][1:]:
                if mail in email_map:
                    ds.unionbysize(i, email_map[mail])
                else:
                    email_map[mail] = i
    
        for i in range(n):
            mails[ds.findUPar(i)].append(i)
        print(mails.items())
        ref = []

        for k, v in mails.items():
            temp = []
            hset = set()
            for i in v:
                for mail in accounts[i][1:]:
                    if mail not in hset:
                        temp.append(mail)
                        hset.add(mail)
            ref.append([accounts[k][0]] + sorted(temp))
        return ref

class DSU:
    
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1] * (n)
        self.cnt = n

    def find(self, u, v):
        return self.findUPar(u) == self.findUPar(v)

    def findUPar(self, node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.findUPar(self.parent[node])
        return self.parent[node]

    def unionbysize(self, u, v):
        par_u = self.findUPar(u)
        par_v = self.findUPar(v)
        if par_u == par_v:
            return
        if self.size[par_u] < self.size[par_v]:
            self.parent[par_u] = par_v
            self.size[par_v] += self.size[par_u]
        else:
            self.parent[par_v] = par_u
            self.size[par_u] += self.size[par_v]
        self.cnt -= 1