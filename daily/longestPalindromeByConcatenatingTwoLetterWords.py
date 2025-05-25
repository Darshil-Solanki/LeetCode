class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        cnt = Counter(words)
        ans = 0
        odd_palindrome = 0

        for word in words:
            rev_word = word[::-1]
            if word == rev_word:
                count = cnt[word]
                if count%2:
                    ans += (count-1)*2
                    if odd_palindrome<1:
                        odd_palindrome = 1
                        ans += 2
                else:
                    ans += cnt[word]*2
                del cnt[word]
            elif word in cnt and rev_word in cnt:
                cnt[word] -= 1
                cnt[rev_word] -= 1
                if not cnt[word]: del cnt[word]
                if not cnt[rev_word]: del cnt[rev_word]
                ans += 4
        
        return ans
