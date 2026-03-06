class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        heap = [(0, k)]
        dist = [inf] * (n+1)
        dist[k] = 0
        while heap:
            current_dist, node = heappop(heap)
            if current_dist > dist[node]:
                continue
            for neighbor, nei_dist in graph[node]:
                if current_dist + nei_dist < dist[neighbor]:
                    dist[neighbor] = current_dist + nei_dist
                    heappush(heap, (dist[neighbor], neighbor))
        maxtime = 0
        for time in dist[1:]:
            if time == inf:
                return -1
            maxtime = max(maxtime, time)
        return maxtime