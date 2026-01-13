class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        dset = DSU(n)
        cables = len(connections)
        if cables < n-1:
            return -1
        for edge in connections:
            dset.unionbysize(edge[0], edge[1])
        req = dset.cnt - 1
        return dset.cnt - 1

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