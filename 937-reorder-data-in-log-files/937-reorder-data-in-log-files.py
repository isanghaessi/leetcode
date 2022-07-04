class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        alphaLogs = []
        numberLogs = []
        for log in logs:
            if log.split(' ')[1].isalpha():
                alphaLogs.append(log)
            else:
                numberLogs.append(log)
        alphaLogs.sort(key = lambda a:(a.split()[1:], a.split()[0]))
        
        return alphaLogs + numberLogs