class Solution:
    def totalMoney(self, n: int) -> int:
        amount = 0
        a = 1
        for _ in range(n//7):
            amount += (21+7*a)
            a+=1

        if n%7:
            for _ in range(n%7):
                amount += a
                a+=1

        return amount
