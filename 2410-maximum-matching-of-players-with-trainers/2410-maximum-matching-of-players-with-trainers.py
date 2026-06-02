class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        plen = len(players)
        tlen = len(trainers)
        players.sort()
        trainers.sort()
        res = 0
        p, t = 0, 0
        while p < plen and t < tlen:
            if players[p] <= trainers[t]:
                res += 1
                p += 1
                t += 1
            else:
                t += 1
        return res