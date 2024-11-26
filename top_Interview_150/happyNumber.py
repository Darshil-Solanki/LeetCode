class Solution:
    def isHappy(self, n: int) -> bool:
        squareMap={
            "0":0, "1":1, "2":4, "3":9, "4":16, "5":25, "6":36,
            "7":49, "8":64, "9":81
        }
        hashMap={}
        while n!=1:
            if n in hashMap:
                return False
            temp=0
            for i in str(n):
                temp+=squareMap[i]
            hashMap[n]=n
            n=temp
            
        return True
        
        
