class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder_hash = defaultdict(bool)
        folder.sort()
        ans = []
        for f in folder:
            curr_hash = ""
            for sub_folder in f.split("/"):
                if not sub_folder:
                    continue
                curr_hash += "_"+sub_folder
                if curr_hash in folder_hash:
                    break
            else:
                ans.append(f)
                folder_hash[curr_hash] = True
        
        return ans

        # as we have sorted folder which means parent will come first and child next adjacent element 
        # using this to efficiently find sub-folders 
        # folder.sort()
        # res = []
        # for path in folder:
        #     if not res or not path.startswith(res[-1] + '/'):
        #         res.append(path)
        # return res
