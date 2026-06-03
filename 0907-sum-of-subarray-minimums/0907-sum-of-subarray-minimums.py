class Solution:
    def sumSubarrayMins(self, nums: List[int]) -> int:
        MOD = (10 ** 9) + 7
        n = len(nums)
        st = []
        res = 0
        nse = [n] * n
        psee = [-1] * n
        for i in range(n-1, -1, -1):
            while st and nums[st[-1]] >= nums[i]:
                st.pop()
            if st:nse[i] = st[-1]
            st.append(i)
        st = []
        for i in range(n):
            while st and nums[st[-1]] > nums[i]:
                st.pop()
            if st:psee[i] = st[-1]
            st.append(i)
        for i in range(n):
            res += ((nse[i] - i) * (i - psee[i]) * nums[i]) % MOD
        return res % MOD