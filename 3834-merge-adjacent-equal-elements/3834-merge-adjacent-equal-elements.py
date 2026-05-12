class Solution:
    def mergeAdjacent(self, nums: List[int]) -> List[int]:
        st = []
        for x in nums:
            while st and st[-1] == x:
                el = st.pop()
                el += x
                x = el
            st.append(x)
        return st