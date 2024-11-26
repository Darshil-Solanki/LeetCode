class Solution:
    def convert(self, s, numRows):
        if numRows==1:
            return s
        temp = []
        for i in range(numRows):
            temp.append([])
        flag = True
        irange = 0
        for i in s:
            if flag:
                temp[irange].append(i)
                irange+=1
                if irange==numRows:
                    flag=False
                    irange-=2
            else:
                temp[irange].append(i)
                irange-=1
                if irange==-1:
                    flag=True
                    irange=1
        return "".join(map("".join, temp))
    # Better Solution using string instead of character list
	# def convert(self, s: str, numRows: int) -> str:
    #     lines = ['' for i in range(numRows)]
    #     i = 0
    #     n = 0
    #     while i < len(s):
    #         if n < numRows:
    #             lines[n] += s[i]
    #         else:
    #            n -= 2
    #            while n > 0 and i < len(s):
    #                 lines[n] += s[i]
    #                 n -= 1
    #                 i += 1
    #             else:
    #                 n = 0
    #             continue
    #         i += 1
    #         n += 1
    #     return ''.join(lines)
