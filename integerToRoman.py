class Solution:
    def intToRoman(self, num: int) -> str:
        data = {1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M'}
        res = ""
        for i,val in enumerate(str(num)[::-1]):
            val = int(val)
            zero = 1 if i==0 else 10**i
            curr = val*zero
            if val in data:
                res = data[curr]+res
            elif val==4:
                res = data[zero]+data[5*zero]+res
            elif val==9:
                res = data[zero]+data[10*zero]+res
            elif val>5:
                res = data[5*zero]+(val-5)*data[zero]+res
            else:
                res=data[zero]*val+res
        return res
        # Great solution 
        # to_r = {
        #     1000: 'M',
        #     900: 'CM',
        #     500: 'D',
        #     400: 'CD',
        #     100: 'C',
        #     90: 'XC',
        #     50: 'L',
        #     40: 'XL',
        #     10: 'X',
        #     9: 'IX',
        #     5: 'V',
        #     4: 'IV',
        #     1: 'I'
        # }
        # roman = ''
        # for i in to_r:
        #     while i <= num:
        #         num -= i
        #         roman += to_r[i]
        # return roman
