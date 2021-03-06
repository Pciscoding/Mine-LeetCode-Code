``Python
538. 把二叉搜索树转换为累加树
思路：把dict类型作为参数传递，则可以使得实参实时改变，也就是说在递归中更深一层的操作可以影响到上一层
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(root, sum: dict):
            if not root:
                return
            dfs(root.right, sum_dict)
            root.val += sum_dict['sum']
            sum_dict['sum'] = root.val
            dfs(root.left, sum_dict)
            return
        
        sum_dict = {'sum': 0}
        dfs(root, sum_dict)
        return root
``
