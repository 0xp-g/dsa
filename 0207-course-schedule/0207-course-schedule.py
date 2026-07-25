class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        graph = defaultdict(list)
        indegree = dict()
        for a, b in prerequisites:
            indegree[a] = 0
            indegree[b] = 0
            graph[a].append(b)
        for k in graph.keys():
            for node in graph[k]:
                indegree[node] += 1
        dq = deque()
        for k, v in indegree.items():
            if v == 0:
                dq.append(k)
        processed = 0
        while dq:
            node = dq.popleft()
            print(node)
            processed += 1
            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    dq.append(nei)
        print(processed, numCourses)
        return processed == len(graph)