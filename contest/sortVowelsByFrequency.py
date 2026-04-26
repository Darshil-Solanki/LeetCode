class Solution:
    def sortVowels(self, s: str) -> str:
        vowels, first_occurences = {}, {}
        for i, c in enumerate(s):
            if c in "aeiou":
                if c in vowels:
                    vowels[c] += 1
                else:
                    vowels[c] = 1
                    first_occurences[c] = i
        temp = []
        for c, cnt in vowels.items():
            temp.append((cnt, first_occurences[c], c))
        temp.sort(key = lambda x: (-x[0], x[1]))
        vowels = deque([])
        for freq, _, c in temp:
            vowels.extend([c]*freq)

        res = []
        for c in s:
            if c in "aeiou":
                res.append(vowels.popleft())
            else:
                res.append(c)
        return "".join(res)
