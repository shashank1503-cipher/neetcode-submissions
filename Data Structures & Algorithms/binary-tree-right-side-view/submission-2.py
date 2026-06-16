# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        levels = []
        if not root:
            return levels
        q.append(root)
        while q:
            n = len(q)
            level = []
            for _ in range(n):
                node = q.popleft()
                level.append(node.val)
                node.left and q.append(node.left)
                node.right and q.append(node.right)
            levels.append(level)
        ans = []
        for level in levels:
            ans.append(level[-1])
        return ans