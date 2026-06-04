class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        n = len(nums)
        res = []
        for i in range(k):
            while dq and dq[0] <= i - k:
                dq.popleft()
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            dq.append(i)
        res.append(nums[dq[0]])
        for i in range(k, n):
            while dq and dq[0] <= i - k:
                dq.popleft()
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            dq.append(i)
            res.append(nums[dq[0]])
        return res
