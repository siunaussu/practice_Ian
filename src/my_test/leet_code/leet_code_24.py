"""
    leet_code_swap_nodes_in_pairs
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # dummy node simplifies head‑swap logic
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while prev.next and prev.next.next:
            # mark the two nodes to swap
            node1 = prev.next
            node2 = prev.next.next

            # perform swap
            prev.next = node2
            node1.next = node2.next
            node2.next = node1

            # move prev forward for next pair
            prev = node1

        return dummy.next

