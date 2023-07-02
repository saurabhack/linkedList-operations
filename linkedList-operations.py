class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedLists:
    def __init__(self):
        self.head=None
    def adfirst(self,data):
        New_node=node(data)
        if self.head==None:
            self.head=New_node
            return
        New_node.data=data
        New_node.next=self.head
        self.head=New_node

    def addLast(self,data):
        New_node=node(data)
        if self.head==None:
            self.head=New_node
            return
        current=self.head
        while(current.next!=None):
            current=current.next
        current.next=New_node
    def display(self) :
        current=self.head
        while(current!=None):
            print(current.data,end=" ->")
            current=current.next
        print("null")

    def delete(self):
        self.head=self.head.next

    def delete_last(self):
        if self.head.next==None:
            head=None
            return
        desk1=self.head
        desk2=self.head.next

        while(desk2.next!=None):
            desk2=desk2.next
            desk1=desk1.next
        desk1.next=None


if __name__=="__main__":
    ll=LinkedLists()
    ll.adfirst(100)
    ll.adfirst(10)
    ll.display()
    ll.addLast(200)
    ll.display()
    ll.addLast(400)
    ll.display()
    ll.delete()
    ll.display()
    ll.delete_last()
    ll.display()
    ll.adfirst(1)
    ll.adfirst(2)
    ll.adfirst(3)
    ll.display()

