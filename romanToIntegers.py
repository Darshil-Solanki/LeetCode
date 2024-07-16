class Solution:
    def romanToInt(self, s: str) -> int:
        num = 0
        n = len(s)
        i = 0
        while(i<n):
            if s[i]=="M":
                num+=1000
                i+=1
            elif s[i]=="D":
                num+=500
                i+=1
            elif s[i]=="C":
                if i+1<n:
                    if s[i+1]=="D":
                        num+=400
                        i+=2
                    elif s[i+1]=="M":
                        num+=900
                        i+=2
                    else:
                        num+=100
                        i+=1
                else:
                    num+=100
                    i+=1
            elif s[i]=="L":
                num+= 50
                i+=1
            elif s[i]=="X":
                if i+1<n:
                    if s[i+1]=="L":
                        num+=40
                        i+=2
                    elif s[i+1]=="C":
                        num+=90
                        i+=2
                    else:
                        num+=10
                        i+=1
                else:
                    num+=10
                    i+=1
            elif s[i]=="V":
                num+=5
                i+=1
            elif s[i]=="I":
                if i+1<n:
                    if s[i+1]=="V":
                        num+=4
                        i+=2
                    elif s[i+1]=="X":
                        num+=9
                        i+=2
                    else:
                        num+=1
                        i+=1
                else:
                    num+=1
                    i+=1
            else:
                return "Invalid Number"
        return num
        

# Copied from the best solution for references
# learning: use dictionary for multiple value pair test no if else or match

# class Solution:
#     def romanToInt(self, s: str) -> int:
#         roman_values = {
#             'I': 1,
#             'V': 5,
#             'X': 10,
#             'L': 50,
#             'C': 100,
#             'D': 500,
#             'M': 1000
#         }

#         resp = 0
#         index = 0
#         for element in s:

#             current = roman_values[element]

#             if index + 1 == len(s):
#                 resp = resp + current

#             elif element == 'C' and (s[index+1] == 'M' or  s[index+1] == 'D'):
#                 resp = resp - 100

#             elif element == 'X' and (s[index+1] == 'L' or  s[index+1] == 'C'):
#                 resp = resp - 10

#             elif element == 'I' and (s[index+1] == 'V' or  s[index+1] == 'X'):
#                 resp = resp - 1

#             else:
#                 resp = resp + current

#             index += 1

#         return resp
