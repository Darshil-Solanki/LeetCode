class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        if p=="*": return True
        pleft, pright = p.split("*")
        pright=pright[::-1]
        reverseS = s[::-1]
        left = right = 0
        if pleft:
            left = s.find(pleft)
            if left==-1:
                return False
        if pright:
            right = reverseS.find(pright)
            if right == -1:
                return False
   
        return left+len(pleft)<=len(s)-right-len(pright)

        # copied from submission
        # lst = p.split('*')
        # last = 0
        # for w in lst:
        #     last = s.find(w, last)
        #     if last == -1:
        #         return False
        #     last += len(w)
        # return True
