class Solution:
    def countWordOccurrences(self, chunks: list[str], queries: list[str]) -> list[int]:
        s = "".join(chunks)
        reg = re.compile(r"[a-z]+(?:-[a-z]+)*")
        words = reg.findall(s)
        word_count = Counter(words)
        
        def find_count(qword):
            return word_count[qword]
            
        ans = []
        for qword in queries:
            ans.append(find_count(qword))
        return ans
