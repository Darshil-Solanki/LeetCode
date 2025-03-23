class Solution:
    def canChange(self, start: str, target: str) -> bool:
        n = len(start)
        start_idx, target_idx = [], []
        start_obj, target_obj = [], []
        for i in range(n):
            if start[i]!="_":
                start_idx.append((start[i], i))
                start_obj.append(start[i])
            if target[i]!="_":
                target_idx.append((target[i], i))
                target_obj.append(target[i])
        if "".join(start_obj)!="".join(target_obj): return False

        for st, t in zip(start_idx, target_idx):
            if st[0]=="L":
                if st[1]<t[1]: return False
            else:
                if st[1]>t[1]: return False
                pass
        
        return True

        # better way same logic (combined both loops)
        # n=len(start)
        # start+="#"
        # target+="#"
        # i, j=0, 0
        # while i<n or j<n:
        #     while i<n and start[i]=='_': i+=1
        #     while j<n and target[j]=='_': j+=1
        #     c=start[i]
        #     if c!=target[j]: return False
        #     if c=='L' and i<j: return False
        #     if c=='R' and i>j: return False
        #     i+=1
        #     j+=1
        # return True
