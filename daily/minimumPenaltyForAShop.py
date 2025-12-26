class Solution:
    def bestClosingTime(self, customers: str) -> int:
        best_hour, min_penatly = -1, float("inf")
        n_tot = y_tot = 0
        n_prefix, y_suffix = [0], [0]
        for c_flag in customers:
            if c_flag=="N":
                n_tot += 1
            n_prefix.append(n_tot)

        for c_flag in customers[::-1]:
            if c_flag=="Y":
                y_tot += 1
            y_suffix.append(y_tot)
        y_suffix = y_suffix[::-1]
        
        for i, (n, y) in enumerate(zip(n_prefix, y_suffix)):
            if n+y < min_penatly:
                min_penatly = n+y
                best_hour = i

        return best_hour

        # Same thing with math improve runtime
        # c = customers
        # length = len(c)
        # result = 0
        # resultIdx = -1
        # accum = 0
        # for i in range(length):
        #     if c[i] == "Y":
        #         accum += 1
        #     else:
        #         accum -= 1
            
        #     if accum > result:
        #         result = accum
        #         resultIdx = i
        
        # return resultIdx + 1
