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

        def bfs(node):

            if not node: return None

            q = collections.deque()
            oldToNew[node] = Node(node.val)

            q.append(node)

            while q:
                curr = q.popleft()

                for n in curr.neighbors:
                    if n not in oldToNew:
                        oldToNew[n] = Node(n.val)
                        q.append(n)

                    oldToNew[curr].neighbors.append(oldToNew[n])
            return oldToNew[node]
        return bfs(node)