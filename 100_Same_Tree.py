class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isSameTree(self, p, q):
        if not p and not q:
          return True
        
        if not p or not q:
            return False

        return (p.val == q.val and 
                self.isSameTree(p.left, q.left) and 
                self.isSameTree(p.right, q.right))
    

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
    p = [1,2,3]
    q = [1,2,3]
    p = createBST(p)
    q = createBST(q)
    my_object = Solution()
    judgement = my_object.isSameTree(p,q)
    print(judgement)

if __name__ == "__main__":
    main()