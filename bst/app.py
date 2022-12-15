

class Node:
    def __init__(self , value):
        self.value = value
        self.left = None
        self.right = None


class BST: 
    def __init__(self):
        self.root = None
    
    # adding value in tree
    def insert(self , val):
        if not self.root: self.root = Node(val)
        else: self._insert(self.root , val)

    # helper add matheod
    def _insert(self , curr , val):
        
        if curr.value > val:

            if curr.left: self._insert(curr.left , val)
            else: curr.left = Node(val)
        elif curr.value < val:

            if curr.right: self._insert(curr.right , val)
            else: curr.right = Node(val)
        else: pass

    # calculate the hight of a binary tree
    def hight(self):
        if self.root: return self._hight(self.root , 0)
        else: return 0
    # helper mathod of hight 
    def _hight(self , curr , count):

        if curr == None: return count
        return max(self._hight(curr.left , count+1) , self._hight(curr.right , count+1))
        
    # search mathod
    def search(self , val):
        if self.root:
            return self._search(self.root , val)
        else: return False
    # helper search mathod
    def _search(self , curr , val):
        if curr.value == val: return True
        
        if curr.value > val and curr.left: return self._search(curr.left , val)
        elif curr.value < val and curr.right: return self._search(curr.right , val) 

        return False
        






a = BST()

a.insert(5)
a.insert(2)
a.insert(6)
a.insert(3)
a.insert(1)
a.insert(4)

# print(a.tree())
# print(a.hight())

print(a.search(4)) #True
print(a.search(9)) #False





def __inOrder(root):

    if root:
        __inOrder(root.left)
        print(str(root.value) , end=" ")
        __inOrder(root.right)
    return

def __preOrder(root):
    if root:
        print(root.value , end=" ")
        __preOrder(root.left)
        __preOrder(root.right)
    return

def __postOrder(root):
    if root:
        __postOrder(root.left)
        __postOrder(root.right)
        print(root.value , end=" ")
    return
__inOrder(a.root)
print()
__preOrder(a.root)
print()
__postOrder(a.root)

