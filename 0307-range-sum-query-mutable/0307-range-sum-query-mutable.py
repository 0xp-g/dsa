class NumArray:

    def __init__(self, arr: List[int]):
        self.arr = arr
        self.n = len(arr)
        self.bit = [0] * (self.n + 1)

        for i in range(self.n):
            self.bit[i + 1] = arr[i]

        for i in range(1, self.n + 1):
            parent = i + (i & (-i))
            if parent <= self.n:
                self.bit[parent] += self.bit[i]


    def update(self, i: int, val: int) -> None:
        difference = val - self.arr[i] 
        self.arr[i] = val
        i += 1
        while i <= self.n:
            self.bit[i] += difference
            i += i & -i

    def query(self, i:int) -> int:
        i += 1
        res = 0
        while i > 0:
            res += self.bit[i]
            i -= i & -i
        return res

    def sumRange(self, left: int, right: int) -> int:
        return self.query(right) - self.query(left-1)
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)