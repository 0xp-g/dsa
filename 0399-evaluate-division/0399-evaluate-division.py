class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for i in range(len(equations)):
            u, v = equations[i]
            w = values[i]
            graph[u].append((v, w))
            graph[v].append((u, 1/w))
        res = []
        def dfs(source, goal, curr_weight, recstack):
            if source == goal:
                return curr_weight
            recstack.add(source)
            for neighbor, weight in graph[source]:
                if neighbor in recstack:
                    continue
                res = dfs(neighbor, goal, curr_weight * weight, recstack)
                if res > 0:
                    return res
            recstack.remove(source)
            return -1
        for u, v in queries:
            if u not in graph or v not in graph:
                res.append(-1.0)
                continue
            if u == v:
                res.append(1)
                continue
            temp = dfs(u, v, 1,set())
            if not temp:
                res.append(-1.0)
            else:
                res.append(temp)
        return res