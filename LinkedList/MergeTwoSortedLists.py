class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy=ListNode()
        current=dummy
        while list1 or list2:
            if list1.val<list2.val:
                current.next=list1
                list1=list1.next
            else:
                current.next=list2
                list2=list2.next
            current=current.next
        if list1:
            current.next=list1
        else:
            current.next=list2
        return dummy.next



if __name__ == '__main__':
    head  = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(4)
    l1 = head
    head = ListNode(1)
    head.next = ListNode(3)
    head.next.next = ListNode(4)
    l2 = head
    s = Solution()
    print(s.mergeTwoLists(l1, l2))