class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key = lambda x:(-x[0], x[1]))
        maxdef = properties[0][1]
        res = 0
        for i in range(len(properties)):
            if properties[i][1] < maxdef:
                res += 1
            maxdef = max(maxdef, properties[i][1])
        return res 