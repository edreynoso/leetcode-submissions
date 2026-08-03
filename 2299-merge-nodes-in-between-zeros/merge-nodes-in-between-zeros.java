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
    public ListNode mergeNodes(ListNode head) {
        
        ListNode solution = new ListNode(0);

        ListNode copy = solution;

        ListNode curr = head.next;

        int runningSum = 0;

        while (curr!= null){

            if (curr.val == 0){

                ListNode sum = new ListNode(runningSum);

                copy.next = sum;
                copy = copy.next;

                runningSum = 0;
            }else {
                runningSum += curr.val;
            }

            curr = curr.next;
        }

        return solution.next;
    }
}