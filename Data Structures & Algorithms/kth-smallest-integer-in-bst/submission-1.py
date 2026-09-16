# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def get_size(self, root):
        if root is None:
            return 0
        return 1 + self.get_size(root.right) + self.get_size(root.left)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # can we index a binary tree node?
        size_left = self.get_size(root.left)
        # root is (size_left + 1)th

        if k == size_left + 1:
            return root.val

        if k <= size_left:
            return self.kthSmallest(root.left, k)
        return self.kthSmallest(root.right, k - size_left - 1)