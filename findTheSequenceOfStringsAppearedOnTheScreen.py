class Solution:
    def stringSequence(self, target: str) -> List[str]:
        initial = ""
        res = []
        for c in target:
            temp = "a"
            while temp!=c:
                res.append(initial+temp)
                temp = chr(ord(temp)+1)
            res.append(initial+temp)
            initial += temp
        return res
