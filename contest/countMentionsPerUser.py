class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        mentions = [0]*numberOfUsers
        online = [1]*numberOfUsers
        timestamp = [0]*numberOfUsers
        events.sort(key= lambda x: ( int(x[1]), -ord(x[0][0]) ) )
        for i, event in enumerate(events):
            if event[0]=="MESSAGE":
                if event[2]=="ALL":
                    for id in range(len(online)):
                        mentions[id]+=1
                elif event[2]=="HERE":
                    for id,status in enumerate(online):
                        if status:
                            mentions[id]+=1
                        else:
                            if timestamp[id]+60<=int(event[1]):
                                online[id]=1
                                mentions[id]+=1
                else:
                    for user in event[2].split():
                        id = int(user[2:])
                        mentions[id]+=1
            else:
                id = int(event[2])
                online[id]=0
                timestamp[id]=int(event[1])
        return mentions
