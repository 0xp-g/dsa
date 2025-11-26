class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = 0
        map = {}

        for item in arr:
            if item in map:
                map[item] = False
            else:
                map[item] = True

        for item in arr:
            if map[item]:
                count += 1
                if count == k:
                    return item

        return ""