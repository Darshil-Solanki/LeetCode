class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        n, m = len(players), len(trainers)
        i, j = 0, 0
        
        count = 0
        while i<n and j<m:
            p, t = players[i], trainers[j]
            if p<=t:
                i += 1
                j += 1
                count += 1
            else:
                j += 1
        
        return count
