class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:

        MOD = 10**9 + 7 #3 pass solution. this solution uses pse and nse to calculate how much influence does an element has as a minimum value. left area * right area * value itself.
        res = 0
        n = len(arr)
        pse = [-1] * n
        nse = [n] * n
        st1 = []
        st2 = []

        for i, v in enumerate(arr):
            while st1 and v <= arr[st1[-1]]:
                st1.pop()
            if st1:
                pse[i] = st1[-1]
            st1.append(i)

        for i in range(n-1, -1, -1):
            while st2 and arr[i] < arr[st2[-1]]:
                st2.pop()
            if st2:
                nse[i] = st2[-1]
            st2.append(i)

        for i in range(n):
            res += (i - pse[i]) * (nse[i] - i) * arr[i]
        
        return res % MOD