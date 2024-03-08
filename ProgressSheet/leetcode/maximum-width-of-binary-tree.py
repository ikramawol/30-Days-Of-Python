# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        container = defaultdict(list)

        def helper(root, level, formula):
            nonlocal container
            
            if root:
                container[level].append(formula)

                helper(root.left, level+1, (2*formula)+1)
                helper(root.right, level+1, (2*formula)+2)
                
        helper(root, 0, 0)   
        
        maxi = 0
        for i in container:
            val = container[i][-1] - container[i][0]
            maxi = max(val, maxi)
        return maxi + 1 

