class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        needs_map = Counter(t)
        required = len(needs_map)
        window_counts = {}
        formed = 0
        left = 0
        min_len = float('inf')
        ans_indices = (-1, -1)
        for right, char in enumerate(s):
            window_counts[char] = window_counts.get(char, 0) + 1
            if char in needs_map and window_counts[char] == needs_map[char]:
                formed += 1
            while left <= right and formed == required:
                current_len = right - left + 1
                if current_len < min_len:
                    min_len = current_len
                    ans_indices = (left, right)
                left_char = s[left]
                window_counts[left_char] -= 1
                if left_char in needs_map and window_counts[left_char] < needs_map[left_char]:
                    formed -= 1
                left += 1
        return "" if min_len == float('inf') else s[ans_indices[0] : ans_indices[1] + 1]