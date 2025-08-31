class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        friends_set = set(friends)
        ans = []
        
        for o in order:
            if o in friends_set:
                ans.append(o)
        
        return ans
