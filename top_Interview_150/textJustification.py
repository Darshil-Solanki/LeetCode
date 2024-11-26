class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        line, ans = [], []
        curLength = 0
        def justifyLine(line, curLength, flag):
            strLine = ""
            n = len(line)
            if n==1:
                return line[0]+" "*(maxWidth-curLength)
            if flag:
                res = " ".join(line)
                return res+ " "*(maxWidth-len(res))
            spaces = maxWidth-curLength+n-1
            moreSpaceIndex = spaces%(n-1)
            gapSpace = spaces//(n-1)
            for i, w in enumerate(line):
                if i<moreSpaceIndex:
                    strLine += (w+" "*(gapSpace+1))
                elif i==n-1:
                    strLine += w
                else:
                    strLine += (w+" "*gapSpace)
            return strLine
        for i, word in enumerate(words):
            if i==len(words)-1:
                if not line:
                    ans.append(justifyLine([word], len(word), True))
                else:
                    if curLength+len(word)+1<=maxWidth:
                        line.append(word)
                        ans.append(justifyLine(line, curLength+len(word)+1, True))
                    else:
                        ans.append(justifyLine(line, curLength, False))
                        ans.append(justifyLine([word], len(word), True))
            elif not line:
                line.append(word)
                curLength=len(word)
            else:
                if curLength+len(word)+1==maxWidth:
                    line.append(word)
                    ans.append(justifyLine(line, curLength+len(word)+1, False))
                    line=[]
                elif curLength+len(word)+1>maxWidth:
                    ans.append(justifyLine(line, curLength, False))
                    line = [word]
                    curLength = len(word)
                else:
                    line.append(word)
                    curLength+=len(word)+1
        return ans
