class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0

        for op in operations:
            match op:
                case "X++"|"++X":
                    x += 1
                case _ :
                    x -= 1
        
        return x
