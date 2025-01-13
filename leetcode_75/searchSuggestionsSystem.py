class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        root = {}
        for word in products:
            node = root
            for c in word:
                if c not in node:
                    node[c] = {}
                node = node[c]
            node['#']={}

        def getList(node, prefix):
            temp = []
            def backtrack(nd, pref):
                if "#" in nd: 
                    temp.append(pref)
                if not nd: return
                for c in nd:
                    backtrack(nd[c], pref+c)

            backtrack(node, prefix)
            return temp


        res = []
        prefix = ""
        node = root
        for c in searchWord:
            if c not in node:
                break
            prefix += c
            curr = getList(node[c], prefix)
            curr.sort()
            res.append(curr[:3])
            node = node[c]
        if len(res)<len(searchWord):
            for i in range(len(searchWord)-len(res)):
                res.append(list())
        return res

        # faster method
        # res = []
        # products.sort()

        # l, r = 0, len(products) - 1
        # for i, c in enumerate(searchWord):
        #     while l <= r and(len(products[l]) <= i or products[l][i] != c):
        #         l += 1
        #     while l <= r and(len(products[r]) <= i or products[r][i] != c):
        #         r -= 1

        #     temp = list()
        #     remain = r - l + 1
        #     for j in range(min(3, remain)):
        #         temp.append(products[l + j])

        #     res.append(temp)
        # return res
