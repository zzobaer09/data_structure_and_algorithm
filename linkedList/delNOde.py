from module import Printf
from tryf import x




def delNode(head , index):

    if head is None: return

    if index == 0:

        head = head.next
        return head

    curr = head
    pre = head
    count = 0
    while curr:

        if count == index - 1:
            pre = curr
            pre.next = curr.next.next
            curr = None
            return head


        count += 1
        curr = curr.next









x.print()
print(Printf(delNode(x.head , 5)))