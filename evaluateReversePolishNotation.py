class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        valStack = []
        for t in tokens:
            if t=="+":
                soperand = valStack.pop()
                foperand = valStack.pop()
                valStack.append(foperand+soperand)
            elif t=='-':
                soperand = valStack.pop()
                foperand = valStack.pop()
                valStack.append(foperand-soperand)
            elif t=='*':
                soperand = valStack.pop()
                foperand = valStack.pop()
                valStack.append(foperand*soperand)
            elif t=='/':
                soperand = valStack.pop()
                foperand = valStack.pop()
                res = foperand/soperand
                valStack.append( math.floor(res) if res>0 else math.ceil(res) )
            else:
                valStack.append(int(t))
        return valStack[-1]


        
