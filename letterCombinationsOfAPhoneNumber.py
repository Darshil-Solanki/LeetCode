class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        digitMap = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'} 
        res = []
        def backtrack(curr, i):
            if len(curr)==len(digits):
                res.append(curr)
                return
            for c in digitMap[digits[i]]:
                backtrack(curr+c, i+1)
        backtrack("", 0)
        return res

        # for loop techniques
        # queue = ['']
        # for digit in digits:
        #     letters = digitMap[digit]
        #     new_queue = []
            
        #     for combination in queue:
        #         for letter in letters:
        #             new_queue.append(combination + letter)
        #     queue = new_queue
        # return queue
