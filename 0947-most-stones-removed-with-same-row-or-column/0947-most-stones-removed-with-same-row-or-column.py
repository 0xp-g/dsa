class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        rowmap = dict()
        colmap = dict()
        ds = DSU(len(stones))

        for i, (x, y) in enumerate(stones):
            if x in rowmap:
                ds.union(i, rowmap[x])
            else:
                rowmap[x] = i
    
            if y in colmap:
                ds.union(i, colmap[y])
            else:
                colmap[y] = i

        return n - ds.cnt #for each component. we can keep removing each node in the component till only 1 remains
        #another intuitive way is find unique components and its sizes and -1 for each and summate it

class DSU:
    
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1] * (n)
        self.cnt = n

    def find(self, node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, u, v):
        par_u = self.find(u)
        par_v = self.find(v)
        if par_u == par_v:
            return False
        if self.size[par_u] < self.size[par_v]:
            self.parent[par_u] = par_v
            self.size[par_v] += self.size[par_u]
        else:
            self.parent[par_v] = par_u
            self.size[par_u] += self.size[par_v]
        self.cnt -= 1