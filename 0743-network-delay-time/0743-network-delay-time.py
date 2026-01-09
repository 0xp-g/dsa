class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        dist = [float('inf')] * (n + 1)
        pq = [(0, k)]
        dist[k] = 0
        while pq:
            dist_so_far, node = pq.pop()
            if dist_so_far > dist[node]:
                continue
            else:
                for nei, wei in graph[node]:
                    if dist_so_far + wei < dist[nei]:
                        dist[nei] = dist_so_far + wei
                        heappush(pq, (dist_so_far + wei, nei))
        res = float('-inf')
        for i in range(1, n + 1):
            if dist[i] == float('inf'):
                return -1
            res = max(res, dist[i])
        else:
            return res