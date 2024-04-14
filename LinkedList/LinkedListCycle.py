# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
            return False
        slow = head
        fast = head
        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False



if __name__ == '__main__':

    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = head.next
    s = Solution()
    print( s.hasCycle(head))

    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = None
    s = Solution()
    print(s.hasCycle(head))

    head = ListNode(1)
    head.next = head
    s = Solution()
    print(s.hasCycle(head))

    head = None
    s = Solution()
    print(s.hasCycle(head))

    head = ListNode(1)
    s = Solution()
    print(s.hasCycle(head))

