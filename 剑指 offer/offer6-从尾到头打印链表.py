class Node():
    def __init__(self,val):
        self.val = val
        self.next = None

class Linklist():
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def isempty(self):
        return self.head == None

    def add(self,item):
        item = Node(item)
        if(self.isempty()):
            self.head = Node(None)
            self.head.next = item
            self.tail = item
            self.size += 1
        else:
            self.tail.next = item
            self.tail = item
            self.size += 1
def printList1(head):#递归调用
    if(head.next!=None):
        printList(head.next)
    print(head.val)

def printList2(head):#基于栈的思想
    lst = []
    while(head.next != None):
        lst.append(head.next.val)
        head = head.next
    return lst


l = Linklist()
for i in range(10):
    l.add(i)
f = printList2(l.head)
for i in range(len(f)):
    print(f.pop())








