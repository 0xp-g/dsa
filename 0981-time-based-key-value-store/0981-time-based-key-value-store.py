class TimeMap:

    def __init__(self):
        self.keytime = defaultdict(list)
        self.keyvalue = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keytime[key].append(timestamp)
        self.keyvalue[key].append(value)

    def get(self, key: str, timestamp: int) -> str:
        arr= self.keytime[key]
        n = len(arr)
        if n == 0:
            return ''
        idx = bisect_left(arr, timestamp)   
        if  idx == n:
            return self.keyvalue[key][n-1]
        elif idx == 0 and arr[0] > timestamp:
            return ''
        else:
            if self.keytime[key][idx] == timestamp:
                return self.keyvalue[key][idx]
            else:
                return self.keyvalue[key][idx-1]

        
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)