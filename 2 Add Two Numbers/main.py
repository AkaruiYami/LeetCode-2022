from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


l_n = Optional[ListNode]


l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))


def add_two_numbers(l1: l_n, l2: l_n) -> l_n:
    r = ListNode()
    r_tail = r
    carry = 0
    while True:
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0

        carry, out = divmod(v1 + v2 + carry, 10)

        r_tail.val = out
        r_tail.next = ListNode(carry)

        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

        if l1 is None and l2 is None:
            if r_tail.next.val == 0:
                r_tail.next = None
            return r
        r_tail = r_tail.next


r = add_two_numbers(l1, l2)
