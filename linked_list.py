class node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linkedlist1:
    def __init__(self):
        self.start = None

    def insertfirst(self, value):
        newnode = node(value)

        if self.start == None:
            self.start = newnode
        else:
            temp = self.start
            while temp.next != None:
                temp = temp.next
            temp.next = newnode


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
            self.start = self.start.next


mylist = linkedlist1()
mylist.insertfirst(10)
mylist.insertfirst(20)
mylist.insertfirst(30)
mylist.insertfirst(40)
mylist.showlist()
print()
mylist.deletefirst()
mylist.showlist()
