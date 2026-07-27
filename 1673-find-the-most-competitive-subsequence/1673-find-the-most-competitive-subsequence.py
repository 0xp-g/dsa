class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        st = []
        for i in range(n):
            can_pop = len(st) - k + n -i
            while st and st[-1] > nums[i] and can_pop > 0:
                st.pop()
                can_pop -= 1
            if len(st) < k: st.append(nums[i])
        return st