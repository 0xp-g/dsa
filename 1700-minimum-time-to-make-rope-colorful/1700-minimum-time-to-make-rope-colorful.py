class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:

        i = 0
        j = 1
        res = 0

        blank = set()
        
        while j < len(colors):

            if colors[i] == colors[j]:

                if neededTime[i] <= neededTime[j]:

                    res += neededTime[i]
                    i = j          

                else:
                    
                    res += neededTime[j]
                    
                j += 1

            else:

                i = j             
                j += 1

        return res    