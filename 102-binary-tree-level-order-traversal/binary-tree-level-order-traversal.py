# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        queue = deque([])
        res = []

        if root is None:
            return res

        queue.append(root)

        while len(queue) != 0:
            level = []

            for i in range(len(queue)):
                e = queue.popleft()

                level.append(e.val)

                if e.left is not None:
                    queue.append(e.left)

                if e.right is not None:
                    queue.append(e.right)

            res.append(level)

        return res