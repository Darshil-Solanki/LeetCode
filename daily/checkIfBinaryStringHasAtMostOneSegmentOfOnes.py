class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        count = 0
        prev = -1
        for i, c in enumerate(s):
            if c == "1":
                if prev == -1 or prev!=i-1:
                    count += 1
                prev = i
            if count>1:
                return False

        return True           
