class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        res = numBottles
        while numBottles >= numExchange:  
            numBottles = numBottles - numExchange + 1 #+1 (bruh... for fullbottle)
            res += 1
            numExchange += 1
        return res