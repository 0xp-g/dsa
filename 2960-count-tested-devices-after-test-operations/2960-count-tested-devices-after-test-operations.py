class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        tested = 0
        for b in batteryPercentages:
            if b - tested > 0:
                tested += 1
        return tested