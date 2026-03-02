class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for x in prerequisites:
            adj[x[0]].append(x[1])
        color = defaultdict(int)
        def dfs(n):
            color[n] = 1
            for neighbor in adj[n]:
                if color[neighbor] == 1:
                    return True
                if color[neighbor] == 0:
                    if dfs(neighbor):
                        return True
            color[n] = 2
            return False
        for i in range(numCourses):
            if color[i] == 0:
                if dfs(i):
                    return False
        return True