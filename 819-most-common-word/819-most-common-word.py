from collections import *

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        vocas = defaultdict(int)
        voca = ''
        for p in paragraph:
            if p.isalpha():
                voca = voca + p.lower()
            else:
                if len(voca) > 0 and voca not in banned:
                    vocas[voca] = vocas[voca] + 1
                voca = ''
        if len(voca) > 0:
            if voca not in banned:
                    vocas[voca] = vocas[voca] + 1
        
        print(vocas)
        answer = ''
        for v in list(vocas.keys()):
            print(v, vocas[v])
            answer = v if vocas[v] > vocas[answer] else answer
        
        return answer