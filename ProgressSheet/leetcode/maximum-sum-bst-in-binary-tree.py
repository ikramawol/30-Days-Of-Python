# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def BST(root):
            nonlocal ans
            if not root:
                return True, 0, -inf, inf
                
            isbstL, _sumL, maxiL, miniL = BST(root.left)
            isbstR, _sumR, maxiR, miniR = BST(root.right)

            _sum = _sumL + _sumR + root.val
            isbst = False
            if isbstL and isbstR:
                if maxiL < root.val < miniR:
                    isbst = True
                    ans = max(ans, _sum)
            
            maxi = max(maxiL, maxiR, root.val)
            mini = min(miniL, miniR, root.val)

            return isbst, _sum, maxi, mini
            
        BST(root)
        return ans