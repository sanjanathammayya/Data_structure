# Assume that you have unsorted student data in single linked list. Data includes student
# registration number, program and CGPA. Sort the nodes of single linked list based on
# CGPA.

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

        
        

ssl=SingleList()
ssl.AddatHead(2,"BDA",7.89)
ssl.AddatHead(1,"CL",8.0)
ssl.addAtTail(3,"BDA",9.99)
ssl.addAtTail(4,"CL",9.98)
ssl.addAtTail(5,"CL",5.89)
print("before sort (based on CGPA)")
ssl.print()
ssl.sort()
print("after sort (based on CGPA)")
ssl.print()





