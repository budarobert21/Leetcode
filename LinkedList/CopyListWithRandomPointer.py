
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random



class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        # if head == None:
        #     return None
        # current = head
        # new_current=Node(0)
        # while current:
        #     new_current.val=current.val
        #     new_current.next=current.next
        #     new_current.random=current.random
        #     current=current.next
        #     new_current=new_current.next
        #
        # while new_current:
        #     print(new_current.val)
        #     print(new_current.random.val)
        #     print(new_current.next.val)
        #     new_current=new_current.next
        #
        # return new_current
        if not head:
            return None

        #prima data construim duplicate ale nodurilor
        current=head
        while current:
            new_node=Node(current.val)
            new_node.next=current.next
            current.next=new_node
            current=new_node.next

        #a doua oara vom pune pointer ul random pentru fiecare copie
        current=head
        while current:
            current.next.random=current.random.next if current.random else None
            current=current.next.next

        old_list=head
        new_list=head.next
        new_head=head.next
        while old_list:
            old_list.next = old_list.next.next
            if new_list:
                new_list.next = old_list.next.next
            old_list = old_list.next
            if new_list:
                new_list = new_list.next
        return new_head







        # current = head
        # while current:
        #     new_node = Node(current.val)
        #     new_node.next = current.next
        #     current.next = new_node
        #     current = new_node.next
        # current = head
        # while current:
        #     current.next.random = current.random.next if current.random else None
        #     current = current.next.next
        # old_list = head
        # new_list = head.next
        # new_head = head.next
        # while old_list:
        #     old_list.next = old_list.next.next
        #     new_list.next = new_list.next.next if new_list.next else None
        #     old_list = old_list.next
        #     new_list = new_list.next
        # return new_head













        # while current:  # cream o copie a listei prin inserarea unui nod nou intre fiecare nod existent
        #     new_node = Node(current.val)
        #     new_node.next = current.next
        #     current.next = new_node
        #     current = new_node.next #pregatim iteratia urmatoare
        # current = head
        # while current:
        #     current.next.random = current.random.next if current.random else None
        #     current = current.next.next
        # old_list = head
        # new_list = head.next
        # new_head = head.next
        # while old_list:
        #     old_list.next = old_list.next.next
        #     new_list.next = new_list.next.next if new_list.next else None
        #     old_list = old_list.next
        #     new_list = new_list.next
        # return new_head

if __name__ == '__main__':
    head = Node(7)
    head.next = Node(13)
    head.next.next = Node(11)
    head.next.next.next = Node(10)
    head.next.next.next.next = Node(1)
    head.next.random = head
    head.next.next.random = head.next.next.next.next
    head.next.next.next.random = head.next.next
    head.next.next.next.next.random = head
    head.next.next.next.next.next = None
    s = Solution()
    print(s.copyRandomList(head))
    # Output: 7, 13, 11, 10, 1
