class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum % 2 == 1: return []
        ls = []
        for n in range(2, 10**10, 2):
            ne = n + 2
            if (finalSum - n) < ne:
                ls.append(finalSum)
                break
            ls.append(n)
            finalSum -= n
        return ls