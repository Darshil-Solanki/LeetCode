class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        prime = [True]*(right+1)
        prime[0] = prime[1] = False
        for num in range(2, int(right**0.5)+1):
            if prime[num]:
                for multiple in range(num*num, right+1, num):
                    prime[multiple] = False
        
        prime_num = [i for i in range(left, right+1) if prime[i]]
        
        # if right-left>=1452: #twin prime property
        #     for i in range(1, len(prime_num)):
        #         if prime_num[i]-prime_num[i-1]<=2:
        #             return [prime_num[i-1], prime_num[i]]

        if len(prime_num)<2: return [-1, -1]

        diff = float("inf")
        closest_pair = (-1, -1)

        for i in range(1, len(prime_num)):
            curr_diff = prime_num[i]-prime_num[i-1]
            if curr_diff<diff:
                diff = curr_diff
                closest_pair = prime_num[i-1], prime_num[i]

        return closest_pair
        # twin prime property if a range is wide by 1452 there exist a one pair of prime number whose diff is 2 
