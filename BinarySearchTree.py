class BST:
    def __init__(self, key):
        self.key = key
        self.lchild = None
        self.rchild = None

    # function to insert nodes in the Tree
    def insert(self, data):
        if self.key is None:
            self.key = data
            return

        if self.key == data:
            return

        if data < self.key:
            if self.lchild:
                self.lchild.insert(data)

            else:
                self.lchild = BST(data)

        else:
            if self.rchild:
                self.rchild.insert(data)

            else:
                self.rchild = BST(data)

    # function to serarching nodes in the tree
    def search(self, data):
        if self.key is None:
            print("Tree is Empty!")
            return

        if data == self.key:
            print(f"{data} is present is the tree!")
            return

        if data < self.key:
            if self.lchild:
                self.lchild.search(data)

            else:
                print(f"{data} is not present is the tree!")

        else:
            if self.rchild:
                self.rchild.search(data)

            else:
                print(f"{data} is not present is the tree!")

    '''
    In Binary Search Tree (BST) there are only three typers of Traversal Algorithm. They are:
    1. pre-order Traversal Algorithm
    2. in-order Traversal Algorithm
    3. post-order Traversal Algorithm
    '''

    def preorderTraversal(self):
        '''
        In pre-order algorithm we have to visit the root node fist then the Left Sub-Tree(LST)
        and then the Right Sub-Tree(RST)

        root --> L.S.T --> R.S.T

        '''
        if self.key is None:
            print("Tree is Empty!")
            return

        print(self.key, end=" ")  # 1. printing the root-Node
        if self.lchild:
            self.lchild.preorderTraversal()

        if self.rchild:
            self.rchild.preorderTraversal()

    def inorderTraversal(self):
        '''
        In in-order algorithm we have to visit the Left Sub-Tree(LST) fist then the root
        and then the Right Sub-Tree(RST)

        L.S.T --> root -->R.S.T

        '''
        if self.key is None:
            print("Tree is Empty!")
            return

        if self.lchild:
            self.lchild.inorderTraversal()

        print(self.key, end=" ")
        if self.rchild:
            self.rchild.inorderTraversal()

    def postorderTraversal(self):
        '''
        In in-order algorithm we have to visit the Left Sub-Tree(LST) fist then the Right Sub-Tree(RST)
        and then the root node

        L.S.T -->R.S.T --> root

        '''

        if self.key is None:
            print("Tree is Empty!")
            return

        if self.lchild:
            self.lchild.postorderTraversal()

        if self.rchild:
            self.rchild.postorderTraversal()

        print(self.key, end=" ")

    # fucntion to delete the node from the tree
    def delete(self, data):
        if self.key is None:
            print("Tree is Empty!")
            return

        if data < self.key:
            if self.lchild:
                self.lchild = self.lchild.delete(data)

            else:
                print(f"\n{data} not present in the Tree!")

        elif data > self.key:
            if self.rchild:
                self.rchild.delete(data)

            else:
                print(f"\n{data} not present in the Tree!")

        else:
            if self.lchild is None:
                temp = self.rchild  # storing the object reference of rchild
                self = None
                return temp

            if self.rchild is None:
                temp = self.lchild  # storing the object reference of lchild
                self = None
                return temp

            node = self.rchild
            while node.lchild:
                node = node.lchild

            self.key = node.key
            self.rchild = self.rchild.delete(node.key)

        return self

    def retMin(self):
        itr = self.lchild
        while itr.lchild:
            itr = itr.lchild  # searching for the None
        return itr.key  # returning the maximum value in the tree

    def retMax(self):
        itr = self.rchild
        while itr.rchild:
            itr = itr.rchild  # searchig for the None
        return itr.key  # returning the max value in the tree

    def isMin(self, data):
        min_val = self.retMin()
        if data == min_val:
            return True

        else:
            return False

    def isMax(self, data):
        max_val = self.retMax()
        if data == max_val:
            return True

        else:
            return False


if __name__ == "__main__":
    root = BST(10)
    num_list = [6, 3, 1, 6, 98, 3, 7]
    for num in num_list:
        root.insert(num)
    print("Pre Order Travesal:",end=" ")
    root.preorderTraversal()
    print("\nIn Order Travesal:",end=" ")
    root.inorderTraversal()
    print("\nPost Order Travesal:",end=" ")
    root.postorderTraversal()
    print("\nIs Min:", root.isMin(1))
    print("Is Max:", root.isMax(98))
