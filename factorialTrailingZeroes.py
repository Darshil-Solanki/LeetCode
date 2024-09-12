class Solution:
    def trailingZeroes(self, n: int) -> int:
        if not n: return 0
        count2 = count5 = 0
        for i in range(1,n+1):
            while not i%2:
                i//=2
                count2+=1
            while not i%5:
                i//=5
                count5+=1
        return count2 if count2<count5 else count5
        # Better Solution count of 5 will be always minimum 
        # count=0
        # while(n>0):
        #     count+=n//5
        #     n=n//5
        # return count
