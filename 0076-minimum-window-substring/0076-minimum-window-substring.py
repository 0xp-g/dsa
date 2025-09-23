class Solution:
    def minWindow(self, s: str, t: str) -> str:
        needsmap = Counter(t);windowmap = dict()
        reqlen = len(needsmap);formed = 0
        left = 0;ans_indices = [float('-inf'), float('-inf')]
        minlen = float('inf')
        for right in range(len(s)):
            windowmap[s[right]] = windowmap.get(s[right], 0) + 1
            if s[right] in needsmap and needsmap[s[right]] == windowmap[s[right]]:
                formed += 1
            while left <= right and formed == reqlen:
                if right - left + 1 < minlen:
                    minlen = min(minlen, right - left + 1)
                    ans_indices = [left, right]
                windowmap[s[left]] = windowmap.get(s[left], 0) - 1
                if s[left] in needsmap and windowmap[s[left]] < needsmap[s[left]]:
                    formed -= 1
                left += 1
        return "" if minlen == float('inf') else s[ans_indices[0] : ans_indices[1] + 1]