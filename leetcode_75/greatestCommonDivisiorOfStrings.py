class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        res = ""
        n1, n2 = len(str1), len(str2)
        for c1, c2 in zip(str1, str2):
            if c1!=c2:
                break
            res+=c1
        newRes = ""
        temp = ""
        for i, c in enumerate(res):
            temp += c
            if (n1%(i+1)==0 and temp*(n1//(i+1)) == str1 
                and n2%(i+1)==0 and temp*(n2//(i+1)) == str2):
                newRes = temp[:]
        return newRes

        # going from backward for more efficiency
        # l1, l2 = len(str1), len(str2)
        # def isDivisor(l):
        #     if l1%l or l2%l:
        #         return False
        #     f1, f2 = l1//l, l2//l
        #     return str1[:l]*f1 == str1 and f2*str1[:l]==str2
        # for l in range(min(l1, l2), 0, -1):
        #     if isDivisor(l):
        #         return str1[:l]
        # return ''
