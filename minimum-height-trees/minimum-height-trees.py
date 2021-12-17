import collections

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        def delete_leaves():
            nonlocal graph
            nonlocal leaves
            
            if len(leaves) < 1:
                for node in graph.keys():
                    if len(graph[node]) <= 1:
                        leaves.append(node)
            else:
                for leaf in list(leaves)[:]:
                    leaves.pop()
                    for leaf_candidate in graph[leaf]:
                        graph[leaf_candidate].remove(leaf)
                        if len(graph[leaf_candidate]) <= 1 and leaf_candidate not in leaves:
                            leaves.appendleft(leaf_candidate)
                    del graph[leaf]
        
        
        if n < 3:
            
            return [i for i in range(n)]
        graph = collections.defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        leaves = collections.deque()
        while n > 2:
            n -= len(leaves)
            delete_leaves()
    
        return leaves
        