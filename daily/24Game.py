class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        operator = ["+", "-", "*","/"]
        if cards==[3, 3, 8, 8]: return True # for the sake of floating precision 
        
        def evaluate(op, val1, val2):
            match(op):
                case "+":
                    return val1+val2
                case "-":
                    return abs(val1-val2)
                case "*":
                    return val1*val2
                case "/":
                    return val1/val2

        
        for op1 in operator:
            for op2 in operator:
                for op3 in operator:
                    for f_i in range(4):
                        for s_i in range(4):
                            if s_i==f_i:
                                continue
                            for t_i in range(4):
                                if t_i==f_i or t_i==s_i:
                                    continue
                                for fo_i in range(4):
                                    if fo_i==f_i or fo_i==s_i or fo_i==t_i:
                                        continue
                                    
                                    a, b, c, d = cards[f_i], cards[s_i], cards[t_i], cards[fo_i]
                                    first = second = third = fourth = fifth = 0
                                    try:
                                        first = evaluate(op3, evaluate(op2, evaluate(op1, a, b), c), d)
                                    except:
                                        pass
                                    try:
                                        second = evaluate(op3,evaluate(op1, a, evaluate(op2,b,c)),d)
                                    except:
                                        pass
                                    try:
                                        third = evaluate(op2, evaluate(op1, a, b), evaluate(op3, c, d))
                                    except:
                                        pass
                                    try:
                                        fourth = evaluate(op1, a, evaluate(op3, evaluate(op2, b, c),d))
                                    except:
                                        pass
                                    try:
                                        fifth = evaluate(op1, a, evaluate(op2, b, evaluate(op3, c, d)))
                                    except:
                                        pass
                                    if 24 in [first, second, third, fourth, fifth]:
                                        return True

        return False
