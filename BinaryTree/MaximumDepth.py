#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None: return 0
        left=self.maxDepth(root.left)
        right=self.maxDepth(root.right)
        return 1+max(left,right)

#Metoda cu Stiva  
# class Solution(object):
#     def maxDepth(self, root):
#         """
#         :type root: TreeNode
#         :rtype: int
#         """
#         # BFS
#         queue = deque()
#
#         if root:
#             queue.append(root)
#
#         level = 0
#         while queue:
#             for i in range(len(queue)):
#                 node = queue.popleft()
#                 if node.left:
#                     queue.append(node.left)
#                 if node.right:
#                     queue.append(node.right)
#             level += 1
#         return level







if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    solution = Solution()
    print(solution.maxDepth(root))
