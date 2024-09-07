class SingleList:
    class _node_:
        def __init__ (self,reg_num,program,cgpa):
            self.data={"reg_num":reg_num,"program":program,"cgpa":cgpa}
            self.next=None

    def __init__(self):
        self.head=None
        self.tail=None
        self.count=0
    def isEmpty(self):
        return self.count==0
    def getCount(self):
        return self.count
    def AddatHead(self,reg_num,program,cgpa):
        newNode=self._node_(reg_num,program,cgpa)
        if not self.isEmpty():
            newNode.next=self.head
            self.head=newNode
        else:
            self.head=self.tail=newNode
        self.count=self.count+1
    def addAtTail(self,reg_num,program,cgpa):
        newNode=self._node_(reg_num,program,cgpa)
        if not self.isEmpty():
            self.tail.next=newNode
            self.tail=newNode
        else:
            self.head=self.tail=newNode
        self.count=self.count+1
    def print(self):
        cur=self.head
        if not cur:
            print("The list is empty")
            return
        print("List ")
        i=1
        while cur:
            print(i," ",cur.data)
            cur=cur.next
            i=i+1
    def sort(self):
        if self.head is None:
            return None
        swapped=True
        while swapped:
            swapped=False
            cur=self.head
            while cur and cur.next:
                if cur.data["cgpa"]> cur.next.data["cgpa"]:
                    cur.data,cur.next.data=cur.next.data,cur.data
                    swapped=True
                else:
                    cur=cur.next
    def merge(self,list2):
        if self.isEmpty():
            self.head=list2.head
            self.tail=list2.tail

        else:
            self.tail.next=list2.head
            self.tail=list2.tail
        self.count+=1

        
        

sll1=SingleList()
sll2=SingleList()
sll1.AddatHead(2,"BDA",10.0)
sll1.AddatHead(1,"CL",8.0)
sll1.addAtTail(3,"BDA",9.99)
sll1.addAtTail(4,"CL",7.0)
sll1.addAtTail(5,"CL",5.89)

sll2.AddatHead(2,"BDA",1.0)
sll2.AddatHead(1,"CL",2.2)
sll2.addAtTail(3,"BDA",4.99)
sll2.addAtTail(4,"CL",3.98)
sll2.addAtTail(5,"CL",6.89)
print("before sort (based on CGPA)")
sll1.print()
sll2.print()
sll1.merge(sll2)
print("after merge")
sll1.print()
sll1.sort()
print("after sort (based on CGPA)")
sll1.print()





