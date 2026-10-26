/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        // create a linked list node that has the value of 0
        ListNode dummy = new ListNode(0); 
        // makde the current point to the same node that the dummy points to
        ListNode current = dummy; 

        // while the list 1 still has nodes and list2 still has nodes 
        while(list1 != null && list2 !=null){
            // if the value of the current node in list1 is less than or equal to the val in list2
            if(list1.val <= list2.val){
                // the current will now point to the list1 node
                current.next = list1; 
                // the list1 pointer with shift to the next node in its own linked list 
                list1 = list1.next; 
            // the current node in list 1 is greater than the the node in list to
            }else{
                // the current node in the result list with point to wthe list 2 node
                current.next = list2;
                // the list two will shift to the next node in its own list 
                list2 = list2.next;
            }
            //movies the current pointer to the next node in the linked list
            current = current.next; 
        }
        // if one list is longer than the other in the end just add all the remaining nodes to the result linked list 
        if(list1 != null){
            current.next = list1;
        }else{
            current.next = list2; 
        }
        //return the first node of the linked list skipping the dummy node 
        return dummy.next; 
    }
}