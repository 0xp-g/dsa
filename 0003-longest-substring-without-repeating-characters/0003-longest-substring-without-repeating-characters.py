class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        occ = set()
        left = 0
        maxLen = 0
        #this problem exception ??
        #we actually check the validity before adding the right. ??
        #violation checked
        for right in range(len(s)):
            while s[right] in occ:
                occ.remove(s[left])
                left += 1 #the set approach works because of the property that no 2 saame chars can be inside bcos of the recursiv obeyance of the property
            occ.add(s[right])
            maxLen = max(maxLen, right - left + 1)
        return maxLen