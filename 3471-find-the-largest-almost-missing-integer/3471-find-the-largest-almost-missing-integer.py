class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        hmap = Counter()
        res = []
        ls = []

        for i in range(n-k+1):
            arr = set()
            for j in range(i, i + k):
                arr.add(nums[j])
            print(arr)
            hmap += Counter(arr)

        res = -inf
        for k,v in hmap.items():
            if v == 1:
                res = max(res, k)
        
        return res if res != -inf else -1