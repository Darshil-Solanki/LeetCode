class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        grid = { team:[0]*len(votes[0]) for team in votes[0]}
        # used negative number for sorting order
        for vote in votes:
            for i, team in enumerate(vote):
                grid[team][i]-=1 

        sorted_teams = sorted(votes[0], key = lambda team: (grid[team], team))
        
        return "".join(sorted_teams)
