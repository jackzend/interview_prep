# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build_list(lil):

    dummy = ListNode()
    head = dummy
    for i in lil:
        next = ListNode(i)
        dummy.next = next
        dummy = dummy.next
    return head.next

list1 = [7,7,7,7]
l1 = build_list(list1)

def removeElements(head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head == None:
            return None
        prev = ListNode()
        prev.next = head
        dummy = prev

        while head:
            if head.val == val:
                prev.next = head.next
                head = head.next
            else:
                head = head.next
                print(head)
                prev = prev.next
                print(head)
            if not head:
                break

        return dummy.next
removeElements(l1,7)