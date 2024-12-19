class Solution:
    def compress(self, chars: List[str]) -> int:
        prev = chars[0]
        count = 1
        arrPointer = 0 
        for i, c in enumerate(chars):
            if not i: continue
            if prev == c:
                count+=1
            else:
                chars[arrPointer]=prev
                if count==1:
                    arrPointer+=1
                elif count<10:
                    chars[arrPointer+1]=str(count)
                    arrPointer += 2
                else:
                    for j, cc in enumerate(str(count)):
                        arrPointer+=1
                        chars[arrPointer]=cc
                    arrPointer+=1
                count=1
            prev = c
        chars[arrPointer]=prev
        if count==1: pass
        elif count<10:
            chars[arrPointer+1]=str(count)
            arrPointer += 1
        else:
            for j, cc in enumerate(str(count)):
                arrPointer+=1
                chars[arrPointer]=cc
        return arrPointer+1
