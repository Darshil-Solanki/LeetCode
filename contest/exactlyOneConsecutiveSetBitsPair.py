class Solution:
    def consecutiveSetBits(self, n: int) -> bool:
        n_str = bin(n)[2:]
        length = len(n_str)
        exist = False
        for i in range(1, length):
            if n_str[i]=="1" and n_str[i-1] == "1":
                if exist:
                    return False
                exist = True
        return exist
