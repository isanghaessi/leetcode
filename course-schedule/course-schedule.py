import collections
import copy

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(courses):
            nonlocal answer
            nonlocal prerequisites_dict
            
            if not answer:
                    
                return
            for pre in prerequisites_dict[courses[-1]]:
                if pre in courses:
                    answer = False
                    
                    return
                prerequisites_dict[courses[-1]].remove(pre)
                dfs([*courses, pre])
        
        
        answer = True
        prerequisites_dict = collections.defaultdict(list)
        for course, pre in prerequisites:
            prerequisites_dict[course].append(pre)
        for course in copy.deepcopy(prerequisites_dict).keys():
            dfs([course])
        
        return answer