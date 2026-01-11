class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dq = deque()
        dq.append((src, 0, 0))
        dist = [float('inf')] * n
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))
        while dq:
            node, dsf, depth = dq.popleft()
            if depth > k:
                continue
            for nei, wei in graph[node]:
                if dist[nei] > dsf + wei and depth <= k:
                    dist[nei] = dsf + wei
                    dq.append((nei, dist[nei], depth + 1))
        return dist[dst] if dist[dst] != float('inf') else -1