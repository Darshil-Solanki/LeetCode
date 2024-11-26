class WordDictionary:

    def __init__(self):
        self.root = {}
        self.search_cache = {}

    def addWord(self, word: str) -> None:
        curr = self.root
        self.search_cache = {}
        for c in word:
            if c not in curr:
                curr[c] = {}
            curr = curr[c]
        curr['#']=True
        

    def search(self, word: str) -> bool:
        top = self.root
        if word in self.search_cache: return self.search_cache[word]
        queue = [(word[0], top)]
        for i in range(len(word)-1):
            curr_len = len(queue)
            for j in range(curr_len):
                node, nei = queue.pop(0)
                if node == ".":
                    for c in nei:
                        if c!='#':
                            queue.append((word[i+1], nei[c]))
                else:
                    if node in nei:
                        queue.append((word[i+1], nei[node]))
        if not queue: self.search_cache[word]=False; return False
        for i in range(len(queue)):
            lastNode, nei = queue.pop(0)
            if lastNode == ".": 
                for c in nei:
                    if c!='#' and '#' in nei[c]:
                        self.search_cache[word] = True
                        return True
            else:
                if lastNode in nei and '#' in nei[lastNode]:
                    self.search_cache[word] = True
                    return True
        self.search_cache[word] = False
        return False



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
