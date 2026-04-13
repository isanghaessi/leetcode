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
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode headPrevious = new ListNode();
        headPrevious.next = head;
        remove(headPrevious, head, n);

        return headPrevious.next;
    }

    int remove(ListNode previous, ListNode current, int n) {
        if (current == null) {
            return 0;
        }
    
        int reverseIndex = remove(current, current.next, n) + 1;

        if (reverseIndex == n) {
            previous.next = current.next;
        }

        return reverseIndex;
    }
}