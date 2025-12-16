from typing import Optional

# Definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Function to print linked list
def print_list(head: Optional[ListNode]):
    curr = head
    while curr:
        print(curr.val, end=" -> " if curr.next else "")
        curr = curr.next
    print()

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev

# -----------------------------
# Input from user
# -----------------------------
values = input("Enter linked list values separated by space: ").split()
values = [int(v) for v in values]  # convert input strings to integers

# Create linked list from user input
if values:
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
else:
    head = None

# Print original list
print("Original list:")
print_list(head)

# Reverse linked list
solution = Solution()
reversed_head = solution.reverseList(head)

# Print reversed list
print("Reversed list:")
print_list(reversed_head)
