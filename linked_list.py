class node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linkedlist1:
    def __init__(self):
        self.start = None

    def insertlast(self, value):
        newnode = node(value)

        if self.start == None:
            self.start = newnode
        else:
            temp = self.start
            while temp.next != None:
                temp = temp.next
            temp.next = newnode
        print("inserting last", value)


    def showlist(self):
        if self.start == None:
            print("list is empty")
        else:
            temp = self.start
            while temp != None:
                print(temp.data, end=' ')
                temp = temp.next

    def deletefirst(self):
        if self.start == None:
            print("list is empty")
        else:
            node = self.start.data
            self.start = self.start.next
        print("deleting first node", node)


    def insertfirst(self, value):
        newnode = node(value)
        if self.start == None:
            self.start=newnode
        else:
            newnode.next = self.start
            self.start = newnode
        print("insert first", value)

    def deletelast(self):
        if self.start == None:
            print("list is empty")
        elif self.start.next == None:
            self.start = None
        else:
            temp = self.start
            while temp.next.next != None:
                temp = temp.next
            temp.next = None
        print("deleting last node")


mylist = linkedlist1()
mylist.insertlast(10)
mylist.insertlast(20)
mylist.insertlast(30)
mylist.insertlast(40)
mylist.showlist()
print()
mylist.insertfirst(50)
mylist.showlist()
print()
mylist.deletefirst()
mylist.showlist()
print()
mylist.deletelast()
mylist.showlist()
