# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p == None and q == None:
            return True
        elif p == None:
            return False
        elif q == None:
            return False

        if p.val!=q.val:
            return  False
        else:
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)







if __name__ == '__main__':
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(3)
    q = TreeNode(1)
    q.left = TreeNode(2)
    q.right = TreeNode(3)
    solution = Solution()
    print(solution.isSameTree(p, q))
