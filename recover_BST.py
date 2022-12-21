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
        
        # create a list to hold the nodes
        temp_list =[]
        
        
        # append the nodes to the temp list 
        def map(node):
            if not node:return
            map(node.left)
            temp_list.append(node)
            map(node.right)
        
        
        map(root)
        
        ## sort the nodes by value
        sorted_list = sorted(n.val for n in temp_list)

        
        # replace the sorted values with original array
        for i in range(len(sorted_list)):
            temp_list[i].val = sorted_list[i]