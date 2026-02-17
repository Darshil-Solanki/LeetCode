class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        ans = []
        for hour in range(12):
            for minutes in range(60):
                if bin(hour).count("1")+bin(minutes).count("1") == turnedOn:
                    ans.append(f"{hour}:{minutes:02d}")
        
        return ans
