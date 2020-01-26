# https://leetcode.com/problems/intersection-of-two-linked-lists/

def getIntersectionNode(self, headA, headB):
    """
    :type head1, head1: ListNode
    :rtype: ListNode
    """
    # check if either linked list is empty
    if headA == None and headB == None:
        return None

    # maintain 2 pointers for each linked list and let them traverse through them
    pA = headA
    pB = headB

    # when either reaches the end of the list redirect to the head of other list
    # if they meet at any point it will be at the intersection node
    while pA is not pB:
        if pA == None:
            pA = headB
        else:
            pA = pA.next
        if pB == None:
            pB = headA
        else:
            pB = pB.next
    return pA
