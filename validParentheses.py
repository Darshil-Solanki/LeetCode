class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == ')':
                if len(stack)==0 or stack[-1]!='(':
                    return False
                del stack[-1]
            elif i=='}':
                if len(stack)==0 or stack[-1]!='{':
                    return False
                del stack[-1]
            elif i==']':
                if len(stack)==0 or stack[-1]!='[':
                    return False
                del stack[-1]
            else:
                stack.append(i)
        return not stack
    
    
# class Solution:
#     def isValid(self, s: str) -> bool:
#         # Map of closing to opening brackets
#         bracket_map = {')': '(', '}': '{', ']': '['}
#         stack = []
        
#         for char in s:
#             if char in bracket_map:
#                 # Pop the top element if available, else assign a dummy value
#                 top_element = stack.pop() if stack else '#'
#                 # Check if the popped element matches the corresponding opening bracket
#                 if bracket_map[char] != top_element:
#                     return False
#             else:
#                 # It's an opening bracket, push onto the stack
#                 stack.append(char)
        
#         # If the stack is empty, all brackets are matched
#         return not stack
        
