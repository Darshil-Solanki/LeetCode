class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        st1, st2 = [],[]
        flag = True
        for c1, c2 in zip(s1,s2):
            if c1!=c2:
                st1.append(c1)
                st2.append(c2)
                flag = False
        if flag: return True
        st1.sort()
        st2.sort()
        if (len(st1)==2 and st1==st2): return True
        return False
