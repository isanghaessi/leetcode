from collections import *

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n < 2:
            
            return [0]
        
        graphDict = defaultdict(list)
        for l, r in edges:
            graphDict[l].append(r)
            graphDict[r].append(l)
        leaves = []
        for i in range(n):
            if len(graphDict[i]) == 1:
                leaves.append(i)
        while n > 2:
            n -= len(leaves)
            newLeaves = []
            for leaf in leaves:
                for neighbor in graphDict[leaf]:
                    graphDict[neighbor].remove(leaf)
                    if len(graphDict[neighbor]) == 1:
                        newLeaves.append(neighbor)
            leaves = newLeaves
        
        return leaves