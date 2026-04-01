class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        if "RL" not in directions:
            return healths
        
        stack = []
        n = len(positions)
        indices = list(range(n))
        indices.sort(key=lambda x: positions[x])
        
        for i in indices:
            if directions[i] == "R":
                stack.append(i)
            else:
                while stack and healths[i]>0:
                    top_i = stack.pop()
                    if healths[top_i]>healths[i]:
                        healths[top_i] -= 1
                        healths[i] = 0
                        stack.append(top_i)
                    elif healths[top_i]<healths[i]:
                        healths[i] -= 1
                        healths[top_i] = 0
                    else:
                        healths[i] = 0
                        healths[top_i] = 0
        
        return [healths[i] for i in range(n) if healths[i]>0]
                
