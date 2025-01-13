class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        astr, bstr, cstr = bin(a)[2:], bin(b)[2:], bin(c)[2:]
        astr, bstr, cstr = "0"*(32-len(astr))+astr, "0"*(32-len(bstr))+bstr, "0"*(32-len(cstr))+cstr
        flip = 0
        for ac, bc, cc in zip(astr, bstr, cstr):
            if cc=="0":
                if ac=="1": flip+=1
                if bc=="1": flip+=1
            else:
                if ac=="0" and bc=="0": flip+=1
        return flip

        # copied from submission faster method using bit directly without converting
        # cnt = 0
        # while c or a or b:
        #     cur_c = c&1
        #     cur_a = a&1
        #     cur_b = b&1
        #     if cur_c != (cur_a or cur_b):
        #         cnt +=1
        #         if not cur_c and (cur_a and cur_b):
        #             cnt += 1
        #     c>>=1
        #     b>>=1
        #     a>>=1
        # return cnt
