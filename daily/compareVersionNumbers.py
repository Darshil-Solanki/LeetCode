class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        def convert(x):
            try:
                return int(x)
            except:
                return 0
        num1, num2 =  version1.split("."), version2.split(".")
        num1, num2 = list(map(convert, num1)), list(map(convert, num2))
        i, j = 0, 0
        while i<len(num1) and j<len(num2):
            if num1[i]<num2[j]:
                return -1
            elif num1[i]>num2[j]:
                return 1
            i += 1
            j += 1

        while i<len(num1):
            if num1[i]:
                return 1
            i += 1
        while j<len(num2):
            if num2[j]:
                return -1
            j += 1
        return 0
