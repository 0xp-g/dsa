class Solution:
    def longestPath(self, parent: list[int], s: str) -> int:
        gmax = 1
        graph = defaultdict(list)
        word = dict()

        for i, v in enumerate(parent):
            if v != -1:
                graph[v].append(i)

            word[i] = s[i]

        def dfs(node, last):
            nonlocal gmax
            notValid = False
            if word[node] == last:
                notValid = True

            res = []
            for v in graph[node]:
                res.append(dfs(v, word[node]))

            res.sort()
            if len(res) >= 2:
                gmax = max(gmax, res[-1] + res[-2] + 1)
                
            if res:
                gmax = max(gmax, res[-1]+1)
            
            if notValid:
                return 0
            
            if not res:
                return 1
            
            else:
                gmax = max(gmax, res[-1]+1)
                return res[-1] + 1
        
        dfs(0, None)
        return gmax