class Solution:
    def calculateScore(self, instructions: List[str], values: List[int]) -> int:
        n = len(instructions)
        visited = [False]*n
        score = 0
        i = 0
        
        while -1<i<n:
            if not visited[i]:
                visited[i] = True
                if instructions[i]=="jump":
                    i += values[i]
                else:
                    score += values[i]
                    i += 1
            else:
                break

        return score
