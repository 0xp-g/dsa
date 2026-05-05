class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        pse = [-1] * n
        nse = [n] * n
        st = []
        for i in range(n-1, -1, -1):
            while st and heights[st[-1]] >= heights[i]:
                st.pop()
            if st: nse[i] = st[-1]
            st.append(i)
        st = []
        for i in range(n):
            while st and heights[st[-1]] >= heights[i]:
                st.pop()
            if st: pse[i] = st[-1]
            st.append(i)
        max_height = 0
        for i in range(n):
            max_height = max(max_height, heights[i] * (nse[i] - pse[i] - 1))
        return max_height