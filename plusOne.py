class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i=-1
        n= - len(digits)
        carry = 0
        while i>=n:
            if digits[i]==9:
                digits[i]=0
                carry=1
            else:
                digits[i]+=1
                carry=0
            if not carry:
                break
            i-=1
        if carry:
            digits.insert(0,1)
        return digits
