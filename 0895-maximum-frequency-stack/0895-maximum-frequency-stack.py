class FreqStack:

    def __init__(self):
        self.recent_factor = 0
        self.heap = list()
        self.hmap = defaultdict(int)
        return

    def push(self, val: int) -> None:
        self.hmap[val] += 1
        heapq.heappush(self.heap, (-self.hmap[val], -self.recent_factor, val))
        self.recent_factor += 1
        return

    def pop(self) -> int:
        _, _, val = heapq.heappop(self.heap)
        self.hmap[val] -= 1
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()