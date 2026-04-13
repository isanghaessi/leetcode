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
    public ListNode reverseList(ListNode head) {
        List<Integer> list = toList(head);
        Collections.reverse(list);
        
        return toNode(list);
    }

    List<Integer> toList(ListNode head) {
        List<Integer> list = new ArrayList<>();

        while (head != null) {
            list.add(head.val);
            head = head.next;
        }

        return list;
    }

    ListNode toNode(List<Integer> list) {
        ListNode head = new ListNode();

        ListNode current = head;
        for (Integer value: list) {
            current.next = new ListNode(value);
            current = current.next;
        }

        return head.next;
    }
}