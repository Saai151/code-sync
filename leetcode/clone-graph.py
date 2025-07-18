"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        oldToNew = {}

        def dfs(node):
            if not node:
                return None

            stack = [node]
            oldToNew[node] = Node(node.val)

            while stack:
                curr = stack.pop()
                for n in curr.neighbors:
                    if n not in oldToNew:
                        oldToNew[n] = Node(n.val)
                        stack.append(n)

                    oldToNew[curr].neighbors.append(oldToNew[n])
            return oldToNew[node]
        
        
        return dfs(node)