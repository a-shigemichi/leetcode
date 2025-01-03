class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def rightSideView(self, root):
        if not root:
            return []
        
        result = []
        
        def dfs(node, level):
            if not node:
                return
                
            if level == len(result):
                result.append(node.val)
                
            dfs(node.right, level + 1)
            dfs(node.left, level + 1)
        
        dfs(root, 0)
        return result
        


def createBST(values):
    if not values:
        return None
        
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    
    return root
        
def main():
    values = [1,2,3,None,5,None,4]
    root = createBST(values)
    my_object = Solution()
    judgement = my_object.rightSideView(root)
    print(judgement)

if __name__ == "__main__":
    main()