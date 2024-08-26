class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        newPath=''
        print(path.split('/'))
        for p in path.split('/'):
            if p=='.' or p=="":
                continue
            if p=="..":
                try:
                    stack.pop()            
                except:
                    pass
            else:
                stack.append(p)
        return "/"+ "/".join(stack)
