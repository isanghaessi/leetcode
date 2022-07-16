from collections import *

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(course, preCourses):
            if course in myCourse:
                
                return True
            if course in preCourses:
                
                return False
            
            for cd in courseDict[course]:
                if not dfs(cd, (*preCourses, course)):
                    
                    return False
            myCourse.add(course)
            
            return True
        
        courseDict = defaultdict(list)
        myCourse = set()
        for course, preCourse in prerequisites:
            courseDict[course].append(preCourse)
        for i in range(numCourses):
            if(not dfs(i, ())):
                
                return False
        
        return True