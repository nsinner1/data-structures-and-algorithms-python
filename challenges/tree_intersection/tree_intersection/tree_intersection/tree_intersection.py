class newNode: 
    def __init__(self, key): 
        self.key = key 
        self.left = self.right = None


def printCommon(root1, root2): 
    tree_1 = [] 
    tree_2 = [] 
  
    while 1: 
        if root1: 
            tree_1.append(root1) 
            root1 = root1.left 
        elif root2: 
            tree_2.append(root2) 
            root2 = root2.left 
        elif len(tree_1) != 0 and len(tree_2) != 0: 
            root1 = tree_1[-1]  
            root2 = tree_2[-1]  
            if root1.key == root2.key: 
                print(root1.key, end = " ") 
                tree_1.pop(-1)  
                tree_2.pop(-1) 
                root1 = root1.right  
                root2 = root2.right 
            elif root1.key < root2.key:       
                tree_1.pop(-1) 
                root1 = root1.right  
                root2 = None
            elif root1.key > root2.key: 
                tree_2.pop(-1) 
                root2 = root2.right  
                root1 = None
        else: 
            break
  

def inorder(root): 
    if root: 
        inorder(root.left)  
        print(root.key, end = " ") 
        inorder(root.right) 
  
  
def insert(node, key): 
    if node == None: 
        return newNode(key)  
  
    if key < node.key:  
        node.left = insert(node.left, key)  
    elif key > node.key:  
        node.right = insert(node.right, key) 
          
    return node 
  

if __name__ == '__main__': 
      
    # First tree
    root1 = None
    root1 = insert(root1, 5)  
    root1 = insert(root1, 1)  
    root1 = insert(root1, 10)  
    root1 = insert(root1, 0)  
    root1 = insert(root1, 4)  
    root1 = insert(root1, 7)  
    root1 = insert(root1, 9)  
  
    # Second tree 
    root2 = None
    root2 = insert(root2, 10)  
    root2 = insert(root2, 7)  
    root2 = insert(root2, 20)  
    root2 = insert(root2, 4)  
    root2 = insert(root2, 9) 
  
    print("Tree 1 : ")  
    inorder(root1)  
    print() 
      
    print("Tree 2 : ") 
    inorder(root2) 
    print() 
  
    print("Trees Intersection: ")  
    printCommon(root1, root2) 
      
