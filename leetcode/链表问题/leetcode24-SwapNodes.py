# Definition for singly-linked list.
import gc
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummyHead  = ListNode(0)
        dummyHead.next = head
        p = dummyHead
        while(p.next != None and p.next.next != None):
            p1 = p.next
            p2 = p1.next
            Next = p2.next
            p.next = p2
            p2.next = p1
            p1.next = Next
            p = p1
        reNode = dummyHead.next
        del dummyHead
        gc.collect()
        # gc.collect(dummyHead)
        return reNode


def CreatLinklist(nums):
    if(len(nums)):
        head = ListNode(nums[0])
        cur = head
        for i in nums[1:]:
            cur.next = ListNode(i)
            cur = cur.next
        return head
def printLinklist(head):
    while(head != None):
        print(head.val,end=" ")
        head = head.next



nums = range(10)
linklist = CreatLinklist(nums)
print("The first link:")
printLinklist(linklist)
a = Solution().swapPairs(linklist)
print("\nThe swap link:")
printLinklist(a)
