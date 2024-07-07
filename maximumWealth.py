class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxValue = 0
        for account in accounts:
            temp = sum(account)
            maxValue = temp if temp>maxValue else maxValue
        return maxValue
