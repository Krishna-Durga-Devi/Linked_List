class ListNode:
    def __init__(self, val=0, next=None):
        self.val=val
        self.next=next
class Solution:
    def show(self,head):
        t=head
        while t:
            print(t.val,end=",")
            t=t.next
    def middleNode(self,head: ListNode) -> ListNode:
        slow=head
        fast=head

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        return slow

obj=Solution()
head=ListNode(1)
head.next=ListNode(2)
head.next.next=ListNode(3)
head.next.next.next=ListNode(4)
head.next.next.next.next=ListNode(5)
head=obj.middleNode(head)
obj.show(head)

