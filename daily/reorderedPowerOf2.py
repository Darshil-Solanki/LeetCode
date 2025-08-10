class Solution:
    def reorder_num(self, x):
        return "".join(sorted(str(x)))

    def reorderedPowerOf2(self, n: int) -> bool:
        target = self.reorder_num(n)

        for i in range(31):
            if self.reorder_num(1<<i)==target:
                return True
        
        return False

        # power = 1
        # if n == 1: return True

        # cnt = Counter(str(n))
        # n_key_set = set(cnt.keys())

        # def reorder_check(power):
        #     c = Counter(str(power))
        #     c_key_set = set(c.keys())
        #     if c_key_set != n_key_set: return False
        #     return all(c[key]==val for key, val in cnt.items())

        # while power<int("9"*len(str(n))):
        #     power *= 2
        #     if reorder_check(power):
        #         return True

        # return False
