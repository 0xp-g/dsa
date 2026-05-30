class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        color = [0] * len(graph)
        def dfs(node):
            color[node] = 1
            for nei in graph[node]:
                if color[nei] == 0:
                    if (dfs(nei)):
                        return True
                elif color[nei] == 1:
                    return True
                else:
                    continue
            color[node] = 2
            return False
        
        for u in range(len(graph)):
            if color[u] == 0:
                dfs(u)

        res = [node for node in range(len(graph)) if color[node] == 2]
        res.sort()
        return res