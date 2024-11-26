class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        count = 0
        table = {}
        for word in bannedWords:
            table[word]=0
        for word in message:
            try:
                table[word]+=1
                count+=1
                if count>1:
                    return True
            except KeyError:
                pass
        return False
