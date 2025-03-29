class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        MOD = 1_000_000_007
        n = len(nums)
        nums_indices = defaultdict(list)
        for i, num in enumerate(nums):
            nums_indices[num].append(i)
        
        # Calculating Prime Score
        prime_score = [0]*n
        for num, indices in nums_indices.items():
            pscore = 0
            for i in range(2, int(sqrt(num))+1):
                if num%i==0:
                    pscore+=1
                    while num%i==0:
                        num//=i
            if num>=2: pscore+=1
            for i in indices:
                prime_score[i] = pscore
        
        # Calculating left dominant and right dominant prime score for each i
        next_dominant, prev_dominant = [n]*n, [-1]*n
        stack = []
        for i, ps in enumerate(prime_score):
            while stack and prime_score[stack[-1]]<ps:
                idx = stack.pop()
                next_dominant[idx] = i
            if stack:
                prev_dominant[i] = stack[-1]
            stack.append(i)

        # Calculate subarray in which i element is dominant
        num_of_subarray = [0]*n
        for i in range(n):
            num_of_subarray[i] = (next_dominant[i]-i) * (i-prev_dominant[i])
        
        max_heap = []
        for i, num in enumerate(nums):
            heappush(max_heap, (-num, i))
        
        # fast exponential
        def _power(base, exp):
            res = 1
            while exp>0:
                if exp%2==1:
                    res = (res*base)%MOD
                base = (base*base) % MOD
                exp//=2
            
            return res

        score = 1
        while k>0:
            num, i = heappop(max_heap)
            num = -num
            operations = min(k, num_of_subarray[i])
            score = (score * _power(num, operations)) % MOD
            k-=operations

        return score

# using cache for seive  of eratosthenes sorting greedy instead of maxheap push operation  and simultaneously calculating score 
# MOD = 10 ** 9 + 7
# MX = 10 ** 5 + 1
# omega = [0] * MX
# for i in range(2, MX): 
#     if omega[i] == 0: 
#         for j in range(i, MX, i): 
#             omega[j] += 1

# class Solution:
#     def maximumScore(self, nums: List[int], k: int) -> int:
#         n = len(nums)
#         left = [-1] * n
#         right = [n] * n
#         st = []
#         for i, v in enumerate(nums): 
#             while st and omega[nums[st[-1]]] < omega[v]: 
#                 right[st.pop()] = i
#             if st: 
#                 left[i] = st[-1]
#             st.append(i)

#         ans = 1
#         for i, v, l, r in sorted(zip(range(n), nums, left, right), key=lambda x: -x[1]): 
#             tot = (i - l) * (r - i)
#             if tot >= k: 
#                 ans = ans * pow(v, k, MOD) % MOD
#                 break
#             ans = ans * pow(v, tot, MOD) % MOD
#             k -= tot
        
#         return ans
