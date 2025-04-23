class Solution:
    def countLargestGroup(self, n: int) -> int:
        def get_sum(num):
            digit_sum = 0
            
            while num>0:
                digit_sum += num % 10
                num //= 10

            return digit_sum
        
        sum_dict = defaultdict(list)
        for num in range(1, n+1):
            sum_dict[get_sum(num)].append(num)
        
        lengths = [len(group) for _, group in sum_dict.items()]
        max_length = max(lengths)
        return lengths.count(max_length)
