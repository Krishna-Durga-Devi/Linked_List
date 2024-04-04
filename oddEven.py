class Node:
    def __init__(self,v):
        self.val=v
        self.next=None
def createLL(n):
    head=None
    for i in  range(n):
        v=input("Enter v :")
        new_node=Node(v)
        if i==0:
            head=new_node
        else:
            t=head
            while t.next:
                t=t.next
            t.next=new_node
    return head
def show(head):
    t=head
    print("\n List:")
    while t:
        print(t.val,end='->')
        t=t.next
def oddeven(head):
    oddhead=head
    evenhead=head.next
    oddt=oddhead
    event=evenhead
    while event and event.next:
        oddt.next=event.next
        oddt=oddt.next
        event.next=oddt.next
        event=event.next
    oddt.next=None
    event.next=None
    print("\n Oddlist:")
    show(oddhead)
    print("\n EvenList:")
    show(evenhead)
n=int(input())
head=createLL(n)
show(head)
oddeven(head)
