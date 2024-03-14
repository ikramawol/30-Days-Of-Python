# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        
        arr = []
        def inorder(root):
            if root:
                inorder(root.left)
                arr.append(root.val)
                inorder(root.right)
        inorder(root)

        def construct(left, right):

            if left > right:
                return

            mid = (left + right)//2

            root = TreeNode(arr[mid])

            root.left = construct(left, mid - 1)
            root.right = construct(mid + 1, right)
            
            return root

        return construct(0, len(arr)-1)