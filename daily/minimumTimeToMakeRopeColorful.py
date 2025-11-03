class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        n = len(colors)
        ans = i = 0
        prev = ""

        while i<n:
            curr = colors[i]
            if curr == prev:
                temp = [neededTime[i-1], neededTime[i]]
                j = i+1
                while j<n and colors[j]==curr:
                    temp.append(neededTime[j])
                    j+=1
                ans += sum(temp)-max(temp)
                i = j-1
            prev = curr
            i += 1
        
        return ans
