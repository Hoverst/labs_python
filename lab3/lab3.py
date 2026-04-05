class BinaryTree: 
    def __init__(self, value, left=None, right=None): 
        self.value = value 
        self.left = left 
        self.right = right 

    def sum_of_depths(self, current_depth=0):

        left_sum = self.left.sum_of_depths(current_depth + 1) if self.left else 0
        right_sum = self.right.sum_of_depths(current_depth + 1) if self.right else 0
        
        return current_depth + left_sum + right_sum

