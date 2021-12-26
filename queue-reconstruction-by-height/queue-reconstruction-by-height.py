class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        answer = []
        people.sort(key = lambda a: (a[0], -a[1]))
        while len(people) > 0:
            height, taller = people.pop()
            count = 0
            index = 0
            for i, a in enumerate(answer):
                if count >= taller:
                    
                    break
                if a[0] >= height:
                    count += 1
                    index = i + 1
            answer.insert(index, [height, taller])
        
        return answer
            