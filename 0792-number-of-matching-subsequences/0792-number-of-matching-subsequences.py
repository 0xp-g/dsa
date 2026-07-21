class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        freq = [[] for _ in range(26)]
        res = 0
        for i, v in enumerate(s):
            freq[ord(v) - ord('a')].append(i)
        last_used = defaultdict(int)
        for word in words:
            flag = True
            lastmap = [-1 for _ in range(26)]
            last_pos = -1
            for ch in word:
                char_idx = ord(ch) - ord('a')
                if not freq[char_idx]:
                    flag = False
                    break
                ans = bisect_left(freq[char_idx],  last_pos + 1)
                if ans == len(freq[char_idx]):
                    flag = False
                    break
                lastmap[char_idx] = ans
                last_pos = freq[char_idx][ans]
            if flag:
                res += 1
        return res