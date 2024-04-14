# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None

        root.left,root.right=root.right,root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

# iterativ
# class Solution(object):
#     def invertTree(self, root):
#         """
#         :type root: TreeNode
#         :rtype: TreeNode
#         """
#         stack = [root]
#         while stack:
#             node = stack.pop()
#             if node:
#                 node.left, node.right = node.right, node.left
#                 stack += node.left, node.right
#         return root


if __name__ == '__main__':
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)
    solution = Solution()
    print(solution.invertTree(root))