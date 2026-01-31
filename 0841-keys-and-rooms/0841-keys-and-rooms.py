class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = [False] * n
        visited[0] = True
        def dfs(node):
            for neighbor in rooms[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    dfs(neighbor)
        dfs(0)
        return False if False in visited else True

