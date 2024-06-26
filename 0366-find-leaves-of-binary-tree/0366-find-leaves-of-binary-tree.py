# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = defaultdict(list)
        def dfs(node):
            if not node:
                return -1
            
            l = dfs(node.left)
            r = dfs(node.right)
            h = max(l, r) + 1
            res[h].append(node.val)
            return h
        
        dfs(root)
        return [vals for _, vals in res.items()]