# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        count = 0
        point = head
        while point != None:
            count += 1
            point = point.next

        point = head
        mid_point = count // 2
        for i in range(mid_point):
            point = point.next
        return point