class DSU:

    def __init__(self, n):
        self.parent = [i for i in range(n+1)]
        self.size = [1] * (n+1)
        self.islands = n

    def find(self, node):
        initial = node
        while self.parent[node] != node:
            node = self.parent[node]
        self.parent[initial] = node
        return node

    def union(self, u, v):

        par1 = self.find(u)
        par2 = self.find(v)
        if par1 == par2:
            return True
        if self.size[par1] > self.size[par2]:
            self.size[par1] += self.size[par2]
            self.parent[par2] = self.parent[par1]

        else:
            self.size[par2] += self.size[par1]
            self.parent[par1] = self.parent[par2]

        self.islands -= 1
        
        return False

class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        ds = DSU(c)
        hmap = defaultdict(list)
        for u, v in connections:
            ds.union(u, v)
        
        for i in range(1, c+1):
            heappush(hmap[ds.find(i)], i)
        
        inactive, res = set(), []
        
        for t, node in queries:
            if t == 1:
                if node not in inactive:
                    res.append(node)
                else:
                    par = ds.find(node)
                    while hmap[par] and hmap[par][0] in inactive:
                        heappop(hmap[par])
                    if hmap[par]:
                        res.append(hmap[par][0])
                    else:
                        res.append(-1)
            else:
                inactive.add(node)

        return res