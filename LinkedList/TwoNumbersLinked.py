# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        dummy = ListNode()
        current = dummy

        while l1 or l2 or carry:
            sum_val = carry

            if l1:
                sum_val += l1.val
                l1 = l1.next
            if l2:
                sum_val += l2.val
                l2 = l2.next

            carry = sum_val // 10
            current.next = ListNode(sum_val % 10)
            current = current.next

        return dummy.next


if __name__ == '__main__':
    s = Solution()
    head = ListNode(2)
    head.next = ListNode(4)
    head.next.next = ListNode(3)
    l1 = head
    head = ListNode(5)
    head.next = ListNode(6)
    head.next.next = ListNode(4)
    l2 = head
    print(s.addTwoNumbers(l1, l2))
    # Output: [7, 0, 8]