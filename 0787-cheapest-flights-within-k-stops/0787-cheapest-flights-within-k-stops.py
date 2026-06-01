class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)

        for u, v, w in flights:
            graph[u].append((v, w))

        INF = float('inf')

        # dist[node][flights_used]
        dist = [[INF] * (k + 2) for _ in range(n)]
        dist[src][0] = 0

        pq = [(0, src, 0)]  # cost, node, flights_used

        while pq:
            cost, node, flights_used = heapq.heappop(pq)

            if node == dst:
                return cost

            if cost > dist[node][flights_used]:
                continue

            if flights_used == k + 1:
                continue

            for nei, price in graph[node]:
                new_cost = cost + price
                new_flights = flights_used + 1

                if new_cost < dist[nei][new_flights]:
                    dist[nei][new_flights] = new_cost
                    heapq.heappush(
                        pq,
                        (new_cost, nei, new_flights)
                    )

        return -1