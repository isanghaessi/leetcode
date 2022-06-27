class Solution:
    result = []
    def partition(self, s: str) -> List[List[str]]:
        # print(s)
        if len(s) < 1:

            return []
        
        result = []
        for i in range(len(s)):
            leftS = s[:i + 1]
            rightS = s[i + 1:]
            if leftS == leftS[::-1]:
                # print('?', s, leftS)
                for foundS in [foundS for foundS in self.partition(rightS) if len(foundS) > 0]:
                    result.append([leftS, *foundS])
        if s == s[::-1]:
            result.append([s])
        
        print(s, result)
        return result