from collections import Counter
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashDict= {}
        sl = list(s)
        tl = list(t)
        for i in range(len(sl)):
            if hashDict.get(sl[i])==None and tl[i] not in hashDict.values():
                hashDict[sl[i]]=tl[i]
            if hashDict.get(sl[i])==None or hashDict.get(sl[i])!=tl[i]:
                return False
        return True
    
# class Solution:
#     def isIsomorphic(self, s: str, t: str) -> bool:
#         if len(s)!=len(t):
#             return False
#         mapST,mapTS={},{}
#         for c1,c2 in zip(s,t):
#             if (c1 not in mapST) and (c2 not in mapTS):
#                 mapST[c1]=c2
#                 mapTS[c2]=c1
#             elif mapST.get(c1)!=c2 or mapTS.get(c2)!=c1:
#                 return False
#         return True
