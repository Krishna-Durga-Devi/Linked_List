class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
class Solution:
    def show(self,head):
        t=head
        count=0
        while t:
            print(t.val,end=",")
            count+=1
            t=t.next
        print("Count:",count)
    def reverseList(self,head):
        prev=None
        while head:
            curr=head
            head=head.next
            curr.next=prev
            prev=curr
        return prev

obj=Solution()
head=ListNode(1)
head.next=ListNode(2)
head.next.next=ListNode(3)
head.next.next.next=ListNode(4)
head=obj.reverseList(head)
obj.show(head)
