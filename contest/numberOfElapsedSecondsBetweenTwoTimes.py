class Solution:
    def secondsBetweenTimes(self, startTime: str, endTime: str) -> int:
        sh, sm, ss = list(map(int, startTime.split(":")))
        eh, em, es = list(map(int, endTime.split(":")))
        if ss>es:
            sm += 1
            s = 60-ss+es
        else:
            s = es-ss
        if sm>em:
            sh += 1
            m = (60 - sm + em) * 60
        else:
            m = (em - sm) * 60
        h = (eh - sh) * 3600
        return h + m + s
