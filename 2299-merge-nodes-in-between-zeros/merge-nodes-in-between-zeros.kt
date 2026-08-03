/**
 * Example:
 * var li = ListNode(5)
 * var v = li.`val`
 * Definition for singly-linked list.
 * class ListNode(var `val`: Int) {
 *     var next: ListNode? = null
 * }
 */
class Solution {
    fun mergeNodes(head: ListNode?): ListNode? {
        
        val solution = ListNode(0);

        var copy = solution;

        var curr = head!!.next;

        var runningSum = 0;

        while (curr != null){

            if (curr.`val` == 0){
                val sum = ListNode(runningSum);

                copy.next = sum;

                copy = copy.next

                runningSum = 0;
            }else {

                runningSum += curr.`val`
            }

            curr = curr.next;
        }

        return solution.next;
    }
}