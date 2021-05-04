# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)


list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)


def mergeTwoLists(l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        a = l1
        b = l2
        dummy = ListNode()  # empty listnode
        head = dummy
        #print(a.val, b.val)
        while a or b: # while a and b are not at the end
            if a and not b:
                dummy.next = ListNode(a.val)
                a = a.next
            elif b and not a:
                dummy.next = ListNode(b.val)
                b = b.next
            elif a.val < b.val:
                dummy.next = ListNode(a.val)
                a = a.next
            else:
                dummy.next = ListNode(b.val)
                b = b.next
            dummy = dummy.next
        head = head.next
        return head


print(mergeTwoLists(list1,list2))