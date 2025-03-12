import random
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val  # value
        self.next = next  # point

    def __repr__(self):
        return f"Node({self.val}, {repr(self.next)})"


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = ListNode(value)
        if not self.head:
            self.head = new_node
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = new_node

    def __repr__(self):
        return repr(self.head)


l1 = LinkedList()
l2 = LinkedList()
l1.append(1)
l1.append(2)
l1.append(4)
l2.append(1)
l2.append(3)
l2.append(4)


def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    sample = ListNode()
    cur = sample
    cur2 = sample

mergeTwoLists(l1, l2)
