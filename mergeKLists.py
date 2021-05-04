from queue import PriorityQueue

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

list1 = [1,4,5]
list2 = [1,3,4]
list3 = [2,6]

l1 = build_list(list1)
l2 = build_list(list2)
l3 = build_list(list3)

inputlist = [l1,l2,l3]


def mergeKLists(lists):
    """
    :type lists: List[ListNode]
    :rtype: ListNode
    """
    class Wrapper():
        def __init__(self, node):
            self.node = node
        def __lt__(self, other):
            return self.node.val < other.node.val

    if len(lists) == 1:
        return lists[0]
    if len(lists) == 0:
        return None
    pq = PriorityQueue()
    for i in range(0,len(lists)):
        a = lists[i]
        if a:
            pq.put(Wrapper(a))

    dummy = ListNode()  # empty listnode
    head = dummy
    while not pq.empty(): # while there is a none empty node in the dictionary
        #min_list_index = min(node_dict, key=lambda x: node_dict[x][0]) # gives us the list index with the smallest current node
        a = pq.get().node
        dummy.next = ListNode(a.val)
        if a.next: # if a has a next node
            pq.put(Wrapper(a.next))
        dummy = dummy.next
    #min_list_index = min(node_dict, key=lambda x: node_dict[x][0]) # returns the ith list that has the smallest val
    return head.next
print(mergeKLists(inputlist))

