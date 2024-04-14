# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):

    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        result = []
        queue = [root]
        while queue:
            result.append(queue[-1].val)
            for i in range(len(queue)): #Interesant queue ul ramane nemodificat doar i ul se modifica in for range ul ramane la fel pe timpul for ului
                node= queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return result

    #practic luam din queue ultimul element care va fi mereu cel din dreapta




if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(4)
    solution = Solution()
    print(solution.rightSideView(root))