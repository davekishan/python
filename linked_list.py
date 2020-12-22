class node:
     def __init__(self, data):
            self.data=data
            self.next=none
            
class linkedlist:
     def __initz__(self):
           self.start=none
     def insertfirst(self, value):
           newnode = node(value)
           if start.next == none:
                self.start=newnode
           else:
                temp = self.start
                while temp.next != none:
                      temp=temp.next
                temp.next = newnode
     
     def showlist(self):
            if self.start == none:
                  print("list is empty")
            else:
                  temp=self.start
                  while temp.next != none:
                        print(temp.data,end=' ')
                        temp=temp.next
     def deletefirst(self):
            if self.start == none:
                  print("list is empty")
            else:
                  self.start=self.start.next
                 
                 

mylist=linkedlist()
mylist.insert(10)
mylist.insert(20)
mylist.insert(30)
mylist.insert(40)
mylist.showlist()
print()
mylist.deletefirst()
mylist.showlist()

             
