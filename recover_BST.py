# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        errors = []

        def catch(node, left, right):
            print(":")
            if node:
                if not(node.val > left and node.val < right):
                    errors.append(node.val)
                return catch(node.left,left, node.val) and  catch(node.right, node.val, right)

        

        catch(root, float("-inf"), float("inf"))