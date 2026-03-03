class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom = Counter(ransomNote)
        magazine = Counter(magazine)
        for k, v in ransom.items():
            if not magazine[k] or magazine[k] < ransom[k]:
                return False
        return True