class Solution:
    def judgeCircle(self, moves: str) -> bool:
        # return moves.count("U") == moves.count("D") and moves.count("L") == moves.count("R")
        x, y = 0, 0
        for m in moves:
            match m:
                case "U":
                    y+=1
                case "D":
                    y-=1
                case "L":
                    x-=1
                case "R":
                    x+=1
        
        return x==0 and y==0
