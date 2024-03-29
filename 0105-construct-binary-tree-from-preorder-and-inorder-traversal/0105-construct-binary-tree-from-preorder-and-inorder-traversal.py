# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        if len(inorder) != len(preorder):
            return None
        n = len(inorder)
        
        # the for loop is taking a lot of compute
        mp = {}
        for i in range(len(inorder)):
            mp[inorder[i]] = i
        
        def construct(prestart, instart, inend):
            
            if inend < instart or prestart >= n:
                return None
            
            root = TreeNode(preorder[prestart])
            inorder_root_index = mp[preorder[prestart]]
            
            left_sub_tree = inorder_root_index - instart
            root.left = construct(prestart+1, instart, inorder_root_index-1)
            root.right = construct(prestart+1 + left_sub_tree, inorder_root_index+1, inend)
            return root
            
        return construct(0, 0, len(inorder)-1)