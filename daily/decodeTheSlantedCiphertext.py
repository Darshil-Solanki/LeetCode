class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        if rows == 1: return encodedText.strip()
        n, m = len(encodedText)//rows, rows

        grid = [encodedText[i*n : i*n+n] for i in range(rows)]

        original = []
        for j in range(n):
            temp = j
            for i in range(rows):
                original.append(grid[i][temp])
                temp += 1
                if temp == n:
                    break
        
        return "".join(original).rstrip()

        # similar approach but calculating index directly faster
        # if rows == 1:
        #     return encoded_text

        # N = len(encoded_text)
        # cols = N // rows
        # i, j, k = 0, 0, 0
        # original_text = []

        # while k < N:
        #     original_text.append(encoded_text[k])
        #     i += 1
        #     if i == rows:
        #         i = 0
        #         j += 1
        #     k = i*(cols + 1) + j

        # return ''.join(original_text).rstrip()
