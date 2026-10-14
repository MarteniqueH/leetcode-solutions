# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        #Set a left pointer at the begining of the linked list 
        left = head

        #while nodes are still avalible and left next node is not null

        while left and left.next:
            #if the current node is equal to the next node 
            #set the next node to the node head of it 

            if left.val == left.next.val:
                left.next = left.next.next

            #if the node and the node next to it are not equal 
            #move the to the next node 

            else:
                left = left.next


        return head