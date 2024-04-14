# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def averageOfLevels(self, root):
        if root is None:
            return []

        result = []
        queue = [root]

        while queue:
            n = len(queue)
            level_sum = 0.0  # Initialize sum for the current level
            for _ in range(n):
                node = queue.pop(0)  # Dequeue node
                level_sum += node.val  # Add node value to the sum
                if node.left:
                    queue.append(node.left)  # Enqueue left child
                if node.right:
                    queue.append(node.right)  # Enqueue right child
            result.append(format(level_sum / n, '.5f'))  # Calculate average with 5 decimal places

        return result





if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    solution = Solution()
    print(solution.averageOfLevels(root))
