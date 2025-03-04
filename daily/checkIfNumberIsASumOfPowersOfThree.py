class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        power = 0
        while n>=3**power:
            power+=1

        while n>0:
            if n>=3**power:
                n-=3**power
            if n>=3**power: return False
            power-=1
        
        return n==0

        # both has same time complexity and runtime but i don't get it how below code usage .20 to .50 mb more space while above does use one more variable "power"
        # while n>0:
        #     if n%3==2:
        #         return False
        #     n//=3
        # return True
