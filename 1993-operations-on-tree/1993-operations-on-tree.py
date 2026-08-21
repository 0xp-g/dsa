class LockingTree:

    def __init__(self, parent: List[int]):
        self.descendant_map = defaultdict(list)
        self.ascendant_map = defaultdict(list)

        self.locked = dict()
        
        for i in range(len(parent)):
            if parent[i] != -1:
                self.descendant_map[parent[i]].append(i)
                self.ascendant_map[i].append(parent[i])
        

    def lock(self, num: int, user: int) -> bool:
        if num in self.locked:
            return False

        self.locked[num] = user
        return True

    def unlock(self, num: int, user: int) -> bool:
        if num not in self.locked:
            return False

        if self.locked[num] == user:
            del self.locked[num]
            return True

        return False

    def upgrade(self, num: int, user: int) -> bool:
        if num in self.locked:
            return False
        
        asc = self.to_do_dfs(num, self.ascendant_map)
        des = self.to_do_dfs(num, self.descendant_map)

        if not des or asc:
            return False

        self.unlock_desc(num, self.descendant_map)

        self.locked[num] = user

        return True
    
    def to_do_dfs(self, node, graph):

        def dfs(node):
            if node == []:
                return False

            if node in self.locked:
                return True
            
            if node not in self.locked and len(graph[node]) == 0:
                return False

            for nei in graph[node]:
                if dfs(nei):
                    return True
            
            return False
        
        res = False

        for nei in graph[node]:
            res = res or dfs(nei)

        return res
    
    def unlock_desc(self, node, graph):
        if node in self.locked:
            del self.locked[node]

        if len(graph[node]) == 0:
            return

        for nei in graph[node]:
            self.unlock_desc(nei, graph)



# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)