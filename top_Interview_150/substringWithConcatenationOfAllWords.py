class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_len = len(words[0])
        num_words = len(words)
        tot_len = word_len*num_words
        word_count = Counter(words)
        ans = []
        for i in range(word_len):
            left = i
            curr_count = Counter()
            for right in range(i, len(s)-word_len+1, word_len):
                word = s[right:right+word_len]
                if word in word_count:
                    curr_count[word]+=1
                    while curr_count[word]> word_count[word]:
                        left_word = s[left:left+word_len]
                        curr_count[left_word]-=1
                        left+=word_len
                    if right + word_len - left == tot_len:
                        ans.append(left)
                else:
                    curr_count = Counter()
                    left = right+word_len
        return ans
