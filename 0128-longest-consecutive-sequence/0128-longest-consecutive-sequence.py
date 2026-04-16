class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        hmap = dict()
        cnt = 1
        for num in nums:
            if num in hmap:
                continue
            else:
                hmap[num] = cnt
                cnt += 1
        
        dsu = DSU(len(nums) + 1, hmap)

        for k in hmap.keys():
            if k + 1 in hmap:
                dsu.union(hmap[k], hmap[k + 1])
            if k - 1 in hmap:
                dsu.union(hmap[k], hmap[k - 1])
        
        return max(dsu.size)
        
class DSU:

    def __init__(self, n, node_map):
        self.par = [i for i in range(n+1)]
        self.size = [1] * (n+1)
    
    
    def find(self, u):
        if self.par[u] != u:
            par_u = self.find(self.par[self.par[u]])
            self.par[u] = par_u
        return self.par[u]
    
    def union(self, u, v):
        par_u = self.find(u)
        par_v = self.find(v)
        if par_u != par_v:
            if self.size[par_u] > self.size[par_v]:
                self.size[par_u] += self.size[par_v]
                self.par[par_v] = par_u
            else:
                self.size[par_v] += self.size[par_u]
                self.par[par_u] = par_v
            return True
        else:
            return False              