# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = ListNode()
        if(head == None):
            return None
        while(head != None):
            Next = head.next
            head.next = pre
            pre = head
            head = Next
        return pre

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
        print(head.val)
        head = head.next



nums = range(10)
linklist = CreatLinklist(nums)
printLinklist(linklist)
# print(a) 