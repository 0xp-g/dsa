class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        cnt = Counter(s)
        total = len(s)
        print(cnt, cnt[letter], total)
        return int((cnt[letter] / total)*100)