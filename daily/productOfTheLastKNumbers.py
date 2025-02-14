class ProductOfNumbers:

    def __init__(self):
        self.prefixProduct = []
        self.zeroIdx = -1

    def add(self, num: int) -> None:
        if not num:
            self.zeroIdx = len(self.prefixProduct)
            if not self.prefixProduct:
                self.prefixProduct.append(1)
            else:
                self.prefixProduct.append(self.prefixProduct[-1])
        else:
            if not self.prefixProduct:
                self.prefixProduct.append(num)
            else:
                self.prefixProduct.append(num*self.prefixProduct[-1])

    def getProduct(self, k: int) -> int:
        if len(self.prefixProduct)-k<=self.zeroIdx<len(self.prefixProduct): return 0
        if k>=len(self.prefixProduct): return self.prefixProduct[-1]
        return self.prefixProduct[-1]//self.prefixProduct[-(k+1)]        

    # faster method
    # reseting prefix array at each new zero because we don't need previous as for that answer will always be zero
    # def __init__(self):
    #     self.pre_mul = []
    #     self.product = 1
        
    # def add(self, num: int) -> None:
    #     if num is not 0:
    #         self.product *= num
    #         self.pre_mul.append(self.product)
    #     else:
    #         self.product = 1
    #         self.pre_mul = []

    # def getProduct(self, k: int) -> int:
    #     if k == len(self.pre_mul):
    #         return self.pre_mul[-1]
    #     elif k > len(self.pre_mul):
    #         return 0
    #     else:
    #         return int(self.pre_mul[-1]/self.pre_mul[-1-k])


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
