class Solution:
    def generateTag(self, caption: str) -> str:
        res = []
        caption = caption.strip()
        l = caption.split()
        count = 0
        for i, word in enumerate(l):
            if not i:
                res.append(word.lower())
                count += len(word)
            else:
                res.append(word[0].upper()+word[1:].lower())
                count += len(word)
            if count==99:
                break
            if count>99:
                res[-1] = res[-1][:99-count]
                break
        return "#" + "".join(res)
