92. 反转链表 II
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head.next or m == n:
            return head
        node1 = ListNode(-1)
        node1.next = head
        for _ in range(m - 1):
            node1 = node1.next
        part1 = node1
        node2 = head
        for _ in range(n):
            node2 = node2.next
        part2 = node2
        pre = part2
        cur = part1.next
        for _ in range(n - m + 1):
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        part1.next = pre
        if m == 1: head = part1.next
        return head
