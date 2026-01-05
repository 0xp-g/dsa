class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        nlen = len(tasks)
        hmap = Counter(tasks)
        k = max(hmap.values())
        cnt = sum(1 for _, v in hmap.items() if v == k)
        return max(nlen, ((k-1) * (n+1)) + cnt)