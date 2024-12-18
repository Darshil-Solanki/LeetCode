from math import ceil
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel = {'a', 'e', 'i', 'o', 'u'}
        newStr, vowelIdx = [], []
        for i, c in enumerate(s):
            if c.isalpha():
                if c.lower() in  vowel: 
                    vowelIdx.append(i)
                    newStr.append(" ")
                    continue
            newStr.append(c)
        n = len(vowelIdx)
        for i in range(ceil(n/2)):
            newStr[vowelIdx[i]], newStr[vowelIdx[n-i-1]] = s[vowelIdx[n-i-1]], s[vowelIdx[i]]
        return "".join(newStr)
