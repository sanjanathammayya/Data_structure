#from dynamicQueue import dynamicQueue
class BST:
    class _node_:
        def __init__(self,ele):
            self.data=ele
            self.left=None
            self.right=None
    def __init__(self):
        self.root=None
        self.count=0
    # a. check BST is empty
    def isEmpty(self):
        return self.count==0
    # b. getcount of nodes
    def getCount(self):
        return self.count
    # c. add node to bst
    def addNode(self,ele):
        cur=parent=self.root
        while cur!=None and ele!=cur.data:
            parent=cur
            if ele<cur.data:
                cur=cur.left
            elif ele>cur.data:
                cur=cur.right
        if cur == None:
            newNode=self._node_(ele)
            if parent==None:
                self.root=newNode
            elif ele< parent.data:
                parent.left=newNode
            elif ele >parent.data:
                parent.right=newNode
            self.count=self.count+1
    # search node
    def isMember(self,ele):
        if not self.isEmpty():
            cur=self.root
            while cur!=None:
                if ele<cur.data:
                    cur=cur.left
                elif ele>cur.data:
                    cur=cur.right
                else:
                    break
            return True
        else:
            return False
    #tree traversal
    # Inorder LPR
    def bstInorder(self):
        if not self.isEmpty():
            self._inorder_(self.root)
    
    def _inorder_(self,node):
        if node:
            self._inorder_(node.left)
            print(node.data,end=" ")
            self._inorder_(node.right)

        # Preorder PLR
    def bstPreorder(self):
        if not self.isEmpty():
            self._Preorder_(self.root)
    
    def _Preorder_(self,node):
        if node:
            print(node.data,end=" ")
            self._Preorder_(node.left)
            self._Preorder_(node.right)
        # Postorder LRP
    def bstPostorder(self):
        if not self.isEmpty():
            self._Postorder_(self.root)
    
    def _Postorder_(self,node):
        if node:
            self._Postorder_(node.left)
            self._Postorder_(node.right)
            print(node.data,end=" ")
    #level order
    def levelorder(self):
        if not self.isEmpty():
            queue=dynamicQueue()
            queue.enqueue(self.root)
            while not queue.is_empty():
                node=queue.dequeue()
                print(node.data,end=" ")
                if node.left:
                    queue.enqueue(node.left)
                if node.right:
                    queue.enqueue(node.right)
    # delete specified node
    # def delete(self,ele):
    #     if not self.isEmpty():
    #         cur=self.root
    #         while cur!=None:
    #             if ele<cur.data:
    #                 cur=cur.left
    #             elif ele>cur.data:
    #                 cur=cur.right
    #             else:
    #                 return cur.data.pop(0)
    #     else:
    #         return False

    # height 
    def bstheight(self):
        if not self.isEmpty():
            return self._height_(self.root)
        else:
            return 0
    
    def _height_(self,node):
        if node is None:
            return 0
        else:
            left=self._height_(node.left)
            right=self._height_(node.right)
            return 1+max(left,right)
        

class dynamicQueue:
    def __init__(self):
        self.queue = []
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def enqueue(self, item):
        self.queue.append(item)
    
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Cannot dequeue.")
            return None
        return self.queue.pop(0)


def main():
    # Test SimpleQueue
    # print("Testing SimpleQueue:")
    bst = BST()
    bst.addNode(50)
    bst.addNode(30)
    bst.addNode(60)
    bst.addNode(70)
    bst.addNode(20)
    bst.addNode(45)

    print("\nCount of nodes:")
    print(bst.getCount())
    print("Is 20 a member?")
    print(bst.isMember(20))
    print("Inorder traversal:")
    bst.bstInorder()
    print("\nPreorder traversal:")
    bst.bstPreorder()
    print("\nPostorder traversal:")
    bst.bstPostorder()
    print("\nLevel order traversal:")
    bst.levelorder()
    # print("delete ", bst.delete(20))
    # print("Inorder traversal:")
    # bst.bstInorder()
    print("\nheight ",bst.bstheight())

if __name__ == "__main__":
    main()

    


            





