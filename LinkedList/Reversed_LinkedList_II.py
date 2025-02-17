# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head # No need to reverse if left == right

        dummy = ListNode(0)
        dumm y.next = head
        prev = dummy

        #Step 1: Move prev to the node before "left"
        for _ in range(left - 1):
            prev = prev.next

        #Step 2: Reverse sublist left to right
        curr = prev.next #points to the first node to reverse(2)
        prev_sublist = None

        for _ in range(right - left + 1):
            temp = curr.next #Store the next value
            curr.next = prev_sublist #Reverse the pointer
            prev_sublist = curr #Move prev_sublist ahead
            curr = temp #Move curr ahead
        
        #Step 3: Reconnect the reversed List
        prev.next.next = curr  # Connect the last node of the reversed part to remaining list
        prev.next = prev_sublist # Connect the first node of the reversed part to previous section
