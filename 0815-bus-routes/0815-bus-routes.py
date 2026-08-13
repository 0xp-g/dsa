class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        graph = defaultdict(list)
        dq = deque()
        vis = set()
        routes = [set(routes[i]) for i in range(len(routes))]
        if source == target:
            return 0
        for i, v in enumerate(routes):
            for d in v:
                if d == source:
                    dq.append((i, 1))
                    vis.add(i)
                graph[d].append(i)

        while dq:
            for _ in range(len(dq)):
                node, stop = dq.popleft()
                for d in routes[node]:
                    if d == target:
                        return stop

                    for n in graph[d]:
                        if n not in vis:
                            dq.append((n, stop + 1))
                            vis.add(n)
        return -1