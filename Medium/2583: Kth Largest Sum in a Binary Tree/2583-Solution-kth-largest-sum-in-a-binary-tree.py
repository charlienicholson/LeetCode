class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        if root is None:
            return -1  # If the tree is empty, return -1
        
        # Initialize a queue for level-order traversal (BFS)
        queue = [root]
        level_sums = []  # To store the sum of each level
        
        while queue: #for every layer
            current_level_sum = 0
            next_level = [] #reset

            for node in queue: #for every node in layer
                #print("---------------")
                #print("LS: ", level_sums)
                current_level_sum += node.val  # Add the node's value to the level sum
                #print("CLS: ",current_level_sum)
                # Add children to next level's queue
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
                #for node in queue: 
                    #print("Queue:", node)
                #print("NL: ",next_level)
                #print("---------------")
            
            # Add the sum of the current level to the list
            level_sums.append(current_level_sum)
            
            # Move to the next level
            queue = next_level

        level_sums.sort(reverse=True)
        if k <= len(level_sums):
            return level_sums[k - 1]
        else:
            return -1  # Return -1 if fewer than k levels exist
