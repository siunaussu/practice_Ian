"""
LeetCode 19: Remove Nth Node From End of List
Complete solution with test cases and visual helpers.
"""

from typing import Optional

# ==================== LIST NODE DEFINITION ====================

class ListNode:
    """Definition for singly-linked list node."""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"ListNode({self.val})"


# ==================== SOLUTION ====================

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Remove the nth node from the end of the list.

        KEY IDEA: Two-Pointer Technique
        - Create a gap of 'n' nodes between two pointers
        - When the lead pointer hits the end, the follow pointer
          is exactly at the node BEFORE the one we need to remove

        Time:  O(L)  — single pass through the list
        Space: O(1)  — only two pointers used
        """

        # Step 0: Both pointers start at the head
        ptr = temp = head

        # Step 1: Advance 'ptr' by n nodes
        # This creates the fixed gap between ptr and temp
        for _ in range(n):
            ptr = ptr.next

        # Step 2: Edge case — if ptr is None, we need to remove the HEAD
        # This happens when n equals the length of the list
        # Example: [1, 2], n=2  →  ptr goes past the end
        if not ptr:
            return head.next

        # Step 3: Move both pointers together until ptr reaches the LAST node
        # The gap of 'n' is preserved, so temp lands at (n+1)th from end
        while ptr.next:
            ptr = ptr.next      # Lead pointer
            temp = temp.next    # Follow pointer (maintains the gap)

        # Step 4: temp is now at the node BEFORE the target
        # Skip the target node by linking around it
        # Before: temp → target → target.next
        # After:  temp → target.next
        temp.next = temp.next.next

        return head


# ==================== HELPER FUNCTIONS ====================

def build_list(values):
    """Create a linked list from a Python list."""
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def list_to_array(head):
    """Convert linked list back to Python list for easy viewing."""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


def print_list(head, name="List"):
    """Pretty print a linked list."""
    arr = list_to_array(head)
    if arr:
        print(f"{name}: {' -> '.join(map(str, arr))} -> null")
    else:
        print(f"{name}: (empty)")


# ==================== TEST CASES ====================

if __name__ == "__main__":

    # print("=" * 60)
    # print("LEETCODE 19: Remove Nth Node From End of List")
    # print("=" * 60)
    #
    # # Test 1: Basic case — remove 2nd from end (node 4)
    print("\n[Test 1] List: [1,2,3,4,5], n=2")
    print("Expected: remove node with value 4")
    head1 = build_list([1, 2, 3, 4, 5])
    print_list(head1, "Before")
    result1 = Solution().removeNthFromEnd(head1, 2)
    print_list(result1, "After ")
    print("Expected: [1, 2, 3, 5]")
    #
    # # Test 2: Remove the HEAD
    # print("\n[Test 2] List: [1,2], n=2")
    # print("Expected: remove node with value 1 (the head)")
    # head2 = build_list([1, 2])
    # print_list(head2, "Before")
    # result2 = Solution().removeNthFromEnd(head2, 2)
    # print_list(result2, "After ")
    # print("Expected: [2]")
    #
    # # Test 3: Remove the TAIL
    # print("\n[Test 3] List: [1,2,3,4,5], n=1")
    # print("Expected: remove node with value 5 (the tail)")
    # head3 = build_list([1, 2, 3, 4, 5])
    # print_list(head3, "Before")
    # result3 = Solution().removeNthFromEnd(head3, 1)
    # print_list(result3, "After ")
    # print("Expected: [1, 2, 3, 4]")
    #
    # # Test 4: Single element list
    # print("\n[Test 4] List: [1], n=1")
    # print("Expected: remove the only node, return empty list")
    # head4 = build_list([1])
    # print_list(head4, "Before")
    # result4 = Solution().removeNthFromEnd(head4, 1)
    # print_list(result4, "After ")
    # print("Expected: []")
    #
    # # Test 5: Three elements, remove middle
    # print("\n[Test 5] List: [1,2,3], n=2")
    # print("Expected: remove node with value 2")
    # head5 = build_list([1, 2, 3])
    # print_list(head5, "Before")
    # result5 = Solution().removeNthFromEnd(head5, 2)
    # print_list(result5, "After ")
    # print("Expected: [1, 3]")
    #
    # # Test 6: Longer list, remove near middle
    # print("\n[Test 6] List: [10,20,30,40,50,60], n=3")
    # print("Expected: remove node with value 40")
    # head6 = build_list([10, 20, 30, 40, 50, 60])
    # print_list(head6, "Before")
    # result6 = Solution().removeNthFromEnd(head6, 3)
    # print_list(result6, "After ")
    # print("Expected: [10, 20, 30, 50, 60]")
    #
    # print("\n" + "=" * 60)
    # print("All tests completed!")
    # print("=" * 60)