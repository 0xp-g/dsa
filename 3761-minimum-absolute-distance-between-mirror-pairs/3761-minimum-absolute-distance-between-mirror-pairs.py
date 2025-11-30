class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        hmap = defaultdict(list)
        res = float('inf')
        for i, v in enumerate(nums):
            v = int(str(v)[::-1])
            hmap[v].append(i)
        print(hmap)
        for i, v in enumerate(nums):
            if v in hmap:
                for idx in hmap[v]:
                    if i > idx:
                        if abs(i - idx) == 1:
                            return 1
                        res = min(res, abs(i - idx))            
        return -1 if res == float('inf') else res