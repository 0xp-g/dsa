class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n, MOD = len(arr), 10 ** 9 + 7
        pse, nsee, st, res = [-1] * n, [n] * n, [], 0
        for i in range(n-1, -1, -1):
            while st and arr[st[-1]] > arr[i]:
                st.pop()
            if st: nsee[i] = st[-1]
            st.append(i)
        st = []
        for i in range(n):
            while st and arr[st[-1]] >= arr[i]:
                st.pop()
            if st: pse[i] = st[-1]
            st.append(i)
        for i in range(n):
            res += arr[i] * (i - pse[i]) * (nsee[i] - i) #(y-x) * (z-y) subarrays
        return res % MOD