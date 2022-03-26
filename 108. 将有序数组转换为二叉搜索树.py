``python
108. 将有序数组转换为二叉搜索树
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        root = TreeNode(nums[len(nums) // 2])
        root.left = self.sortedArrayToBST(nums[0: len(nums) // 2])
        root.right = self.sortedArrayToBST(nums[len(nums) // 2 + 1: len(nums)])
        return root
``
