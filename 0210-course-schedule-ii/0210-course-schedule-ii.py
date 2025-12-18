class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        gph = defaultdict(list)
        for x, y in prerequisites:
            gph[y].append(x)

        visited = set()
        stack = set()
        topo = []

        def dfs(node):

            visited.add(node)
            stack.add(node)

            for n in gph[node]:
                if n in stack:
                    return False
                elif n not in visited and not dfs(n):
                    return False
            stack.remove(node)
            topo.append(node)
            return True

        for x in range(numCourses):
            if x not in visited:
                if not dfs(x): return []
                
        return topo[::-1]