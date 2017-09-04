# Definition for singly-linked list.
#删除倒数第 n 个节点
import gc
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummyHead = ListNode(0)
        dummyHead.next = head
        p = q = dummyHead
        i = 0
        while(q.next != None):
            if( i < n ):
                print(i)
                i += 1
            else:
                p = p.next
            q = q.next
        p.next = p.next.next
        reNode = dummyHead.next
        del dummyHead
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
a = Solution().removeNthFromEnd(linklist, 2)
print("\nThe remove link:")
printLinklist(a)
