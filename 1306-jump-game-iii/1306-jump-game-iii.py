class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        dq = deque()
        n = len(arr)
        dq.append(start)
        visited = set()
        while dq:
            node = dq.popleft()
            if arr[node] == 0:
                return True
            if node in visited:
                continue
            visited.add(node)
            node1 = None if arr[node] + node >= n else arr[node] + node
            node2 = None if node - arr[node] < 0 else -arr[node] + node
            if node1 != None:
                dq.append(node1)
            if node2 != None:
                dq.append(node2)
        return False